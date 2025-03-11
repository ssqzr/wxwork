import json
import requests
import frappe

# frappe.utils.logger.set_log_level("DEBUG")
logger = frappe.logger(__name__)


# 参数	说明
# errcode	返回码
# errmsg	对返回码的文本描述内容
# userid	成员UserID
# gender	性别。0表示未定义，1表示男性，2表示女性。仅在用户同意snsapi_privateinfo授权时返回真实值，否则返回0.
# avatar	头像url。仅在用户同意snsapi_privateinfo授权时返回真实头像，否则返回默认头像
# qr_code	员工个人二维码（扫描可添加为外部联系人），仅在用户同意snsapi_privateinfo授权时返回
# mobile	手机，仅在用户同意snsapi_privateinfo授权时返回，第三方应用不可获取
# email	邮箱，仅在用户同意snsapi_privateinfo授权时返回，第三方应用不可获取
# biz_mail	企业邮箱，仅在用户同意snsapi_privateinfo授权时返回，第三方应用不可获取
# address	仅在用户同意snsapi_privateinfo授权时返回，第三方应用不可获取
class WXWorkUserDetail(object):
    def __init__(
        self, userid, gender, avatar, qr_code, mobile, email, biz_mail, address
    ):
        self.userid = userid
        self.gender = gender
        self.avatar = avatar
        self.qr_code = qr_code
        self.mobile = mobile
        self.email = email
        self.biz_mail = biz_mail
        self.address = address

    @classmethod
    def from_dict(cls, d):
        userid = d.get("userid")
        gender = d.get("gender")
        avatar = d.get("avatar")
        qr_code = d.get("qr_code")
        mobile = d.get("mobile")
        email = d.get("email")
        biz_mail = d.get("biz_mail")
        address = d.get("address")
        return cls(userid, gender, avatar, qr_code, mobile, email, biz_mail, address)

    def __str__(self):
        return json.dumps(self.__dict__)


def _get_token_cache_name(wxwork_app_id):
    return f"wxwork_app_token:{wxwork_app_id}"


def _get_token_from_cache(wxwork_app_id):
    token = frappe.cache.get_value(_get_token_cache_name(wxwork_app_id))
    logger.debug(
        "get wxwork token from cache, wxwork_app_id=%s, token=%s", wxwork_app_id, token
    )
    return token


def _set_token_to_cache(wxwork_app_id, wxwork_token, expire_seconds):
    logger.debug(
        "set wxwork token to cache, wxwork_app_id=%s, token=%s, expire_seconds=%s",
        wxwork_app_id,
        wxwork_token,
        expire_seconds,
    )

    frappe.cache.set_value(
        _get_token_cache_name(wxwork_app_id),
        wxwork_token,
        expires_in_sec=expire_seconds - 1 * 60 * 10,  # 提前10分钟过期
    )


def _get_token_from_wxwork(wxwork_app_id):
    wxwork_app = frappe.get_doc("WXWork APP", wxwork_app_id)
    wxwork_company = frappe.get_doc("WXWork Company", wxwork_app.wx_company)

    logger.debug(
        f"wxwork app doctype=%s, wxwork company doctype=%s", wxwork_app, wxwork_company
    )

    kw = {
        "corpid": wxwork_company.company_id,
        "corpsecret": wxwork_app.get_password("wx_app_secret"),
    }
    response = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=kw)
    token_result = response.json()
    if token_result["errcode"] == 0:
        wxwork_token = token_result["access_token"]
        expire_seconds = token_result["expires_in"]
        return wxwork_token, expire_seconds
    else:
        logger.error(
            "get token from wxwork failed, code=%s, message=%s",
            token_result["errcode"],
            token_result["errmsg"],
        )
        raise Exception(token_result["errmsg"])


# 根据 code 获取用户信息
# 只能获取到 userid 和 user_ticket
# https://developer.work.weixin.qq.com/document/path/91023
def get_wxwork_user_info(wxwork_app_id, code):
    wxwork_token = get_token(wxwork_app_id)
    params = {"access_token": wxwork_token, "code": code}
    resp = requests.get(
        "https://qyapi.weixin.qq.com/cgi-bin/auth/getuserinfo", params=params
    )
    wxwork_user = resp.json()

    if wxwork_user["errcode"] != 0:
        logger.error(
            "get user info from wxwork failed, code=%s, message=%s",
            wxwork_user["errcode"],
            wxwork_user["errmsg"],
        )
        raise Exception(wxwork_user["errmsg"])

    logger.debug("get wxwork user info success, wxwork_user=%s", wxwork_user)
    return wxwork_user["userid"], wxwork_user["user_ticket"]


def get_wxwork_user_detail(wxwork_app_id, user_ticket) -> WXWorkUserDetail:
    wxwork_token = get_token(wxwork_app_id)
    body = {"user_ticket": user_ticket}
    params = {"access_token": wxwork_token}
    resp = requests.post(
        f"https://qyapi.weixin.qq.com/cgi-bin/auth/getuserdetail",
        params=params,
        json=body,
    )
    wxwork_user = resp.json()
    if wxwork_user["errcode"] != 0:
        logger.error(
            "get user detail from wxwork failed, code=%s, message=%s",
            wxwork_user["errcode"],
            wxwork_user["errmsg"],
        )
        raise Exception(wxwork_user["errmsg"])

    logger.debug("get wxwork user detail success, wxwork_user=%s", wxwork_user)

    user = WXWorkUserDetail.from_dict(wxwork_user)
    return user


def get_token(wxwork_app_id):
    wxwork_token = _get_token_from_cache(wxwork_app_id)
    if not wxwork_token:
        wxwork_token, expire_seconds = _get_token_from_wxwork(wxwork_app_id)
        _set_token_to_cache(wxwork_app_id, wxwork_token, expire_seconds)
    return wxwork_token


@frappe.whitelist(allow_guest=True)
def wxwork_login(code, state):
    logger.debug("from wxwork callback, code=%s, state=%s", code, state)
    wxwork_app_id = state
    wxwork_app_doctype = frappe.get_doc("WXWork APP", wxwork_app_id)
    _, wxwork_user_ticket = get_wxwork_user_info(wxwork_app_id, code)
    wxwork_userdetail = get_wxwork_user_detail(wxwork_app_id, wxwork_user_ticket)

    logger.debug("wxwork_userdetail: %s", wxwork_userdetail)

    if not wxwork_userdetail.mobile:
        logger.error("wxwork user mobile is empty, user detail: %s", wxwork_userdetail)
        raise Exception("企业微信用户手机号未设置")

    # 根据手机号查找用户
    try:
        user = frappe.get_all(
            "User",
            filters={"mobile_no": wxwork_userdetail.mobile},
            fields=["name"],
            limit_page_length=1,
        )
    except Exception as e:
        logger.error(
            "get user by mobile error, mobile=%s, error=%s", wxwork_userdetail.mobile, e
        )
        raise

    if not user:
        logger.error("can not found user by mobile(%s)", wxwork_userdetail.mobile)
        raise frappe.DoesNotExistError(doctype="User")

    logger.debug("get user doc by mobile(%s), user=%s", wxwork_userdetail.mobile, user)

    frappe.local.login_manager.login_as(user[0].name)
    frappe.local.response["type"] = "redirect"
    frappe.local.response["location"] = wxwork_app_doctype.app_url
    logger.debug(
        "login as user: %s, redirect to: %s", user[0].name, wxwork_app_doctype.app_url
    )


# 用于企业微信的域名归属认证
# 但是不支持重定向
# @frappe.whitelist(allow_guest=True)
# def wxwork_verify_domain_file(filename):
#     public_file_path = frappe.get_site_path("public", "files", filename)
#     if not os.path.exists(public_file_path):
#         raise frappe.DoesNotExistError

#     with open(public_file_path, "r") as file:
#         response = Response()
#         response.mimetype = "text"
#         filename = filename.encode("utf-8").decode("unicode-escape", "ignore")
#         response.data = file.read()
#         return response
