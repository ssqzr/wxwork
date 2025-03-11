# Copyright (c) 2025, ssqzr and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from urllib.parse import quote_plus, urlparse, urljoin


class WXWorkAPP(Document):

    def validate(self):
        self.wx_app_agentid = self.wx_app_agentid.strip()

        self.wx_app_name = self.wx_app_name.strip()
        if not self.wx_app_name:
            self.wx_app_name = self.wx_app_agentid

        self.wx_app_secret = self.wx_app_secret.strip()
        self.app_url = self.app_url.strip().rstrip("/")

        url = urlparse(self.app_url)
        if not url.scheme or not url.netloc:
            frappe.throw("应用URL格式不正确")

    # 确保 self.name 有值
    def _gen_homepage(self):
        wx_company = frappe.get_doc("WXWork Company", self.wx_company)

        url = urlparse(self.app_url)
        base_url = f"{url.scheme}://{url.netloc}"
        redirect_url = urljoin(
            base_url, "/api/method/wxwork.wxwork.wxwork_service.wxwork_login"
        )
        redirect_url = quote_plus(redirect_url)

        full_url = f"https://open.weixin.qq.com/connect/oauth2/authorize"
        full_url += f"?appid={wx_company.company_id}"
        full_url += f"&redirect_uri={redirect_url}"
        full_url += f"&response_type=code&scope=snsapi_privateinfo"
        full_url += f"&state={self.name}"
        full_url += f"&agentid={self.wx_app_agentid}"
        full_url += "#wechat_redirect"
        return full_url

    def save(self, *args, **kwargs):
        self.wx_homepage = ""
        super().save(*args, **kwargs)
        # self.name 需要保存后才能取到值，并且要保证 self.name 不会改变，不然 wx_homepage
        self.wx_homepage = self._gen_homepage()
        super().save(*args, **kwargs)
