app_name = "wxwork"
app_title = "wxwork"
app_publisher = "ssqzr"
app_description = "企业微信"
app_email = "1596540547@qq.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "wxwork",
# 		"logo": "/assets/wxwork/logo.png",
# 		"title": "wxwork",
# 		"route": "/wxwork",
# 		"has_permission": "wxwork.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/wxwork/css/wxwork.css"
# app_include_js = "/assets/wxwork/js/wxwork.js"

# include js, css files in header of web template
# web_include_css = "/assets/wxwork/css/wxwork.css"
# web_include_js = "/assets/wxwork/js/wxwork.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "wxwork/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "wxwork/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "wxwork.utils.jinja_methods",
# 	"filters": "wxwork.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "wxwork.install.before_install"
# after_install = "wxwork.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "wxwork.uninstall.before_uninstall"
# after_uninstall = "wxwork.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "wxwork.utils.before_app_install"
# after_app_install = "wxwork.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "wxwork.utils.before_app_uninstall"
# after_app_uninstall = "wxwork.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "wxwork.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"wxwork.tasks.all"
# 	],
# 	"daily": [
# 		"wxwork.tasks.daily"
# 	],
# 	"hourly": [
# 		"wxwork.tasks.hourly"
# 	],
# 	"weekly": [
# 		"wxwork.tasks.weekly"
# 	],
# 	"monthly": [
# 		"wxwork.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "wxwork.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "wxwork.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "wxwork.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["wxwork.utils.before_request"]
# after_request = ["wxwork.utils.after_request"]

# Job Events
# ----------
# before_job = ["wxwork.utils.before_job"]
# after_job = ["wxwork.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"wxwork.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# 用于企业微信的域名归属认证
# 但是不支持重定向
# website_redirects = [
#     {
#         "source": r"/(WW_verify_.*)",
#         "target": r"/api/method/wxwork.wxwork.wxwork_service.wxwork_verify_domain_file?filename=\1",
#     }
# ]


app_include_js = "/assets/wxwork/js/wxwork.js"
