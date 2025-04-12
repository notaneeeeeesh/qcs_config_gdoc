app_name = "qcs_config_gdoc"
app_title = "Qcs Config Gdoc"
app_publisher = "QCS"
app_description = "App to configure Google Document AI"
app_email = "support@quarkcs.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "qcs_config_gdoc",
# 		"logo": "/assets/qcs_config_gdoc/logo.png",
# 		"title": "Qcs Config Gdoc",
# 		"route": "/qcs_config_gdoc",
# 		"has_permission": "qcs_config_gdoc.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/qcs_config_gdoc/css/qcs_config_gdoc.css"
# app_include_js = "/assets/qcs_config_gdoc/js/qcs_config_gdoc.js"

# include js, css files in header of web template
# web_include_css = "/assets/qcs_config_gdoc/css/qcs_config_gdoc.css"
# web_include_js = "/assets/qcs_config_gdoc/js/qcs_config_gdoc.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "qcs_config_gdoc/public/scss/website"

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
# app_include_icons = "qcs_config_gdoc/public/icons.svg"

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
# 	"methods": "qcs_config_gdoc.utils.jinja_methods",
# 	"filters": "qcs_config_gdoc.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "qcs_config_gdoc.install.before_install"
# after_install = "qcs_config_gdoc.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "qcs_config_gdoc.uninstall.before_uninstall"
# after_uninstall = "qcs_config_gdoc.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "qcs_config_gdoc.utils.before_app_install"
# after_app_install = "qcs_config_gdoc.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "qcs_config_gdoc.utils.before_app_uninstall"
# after_app_uninstall = "qcs_config_gdoc.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "qcs_config_gdoc.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
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
# 		"qcs_config_gdoc.tasks.all"
# 	],
# 	"daily": [
# 		"qcs_config_gdoc.tasks.daily"
# 	],
# 	"hourly": [
# 		"qcs_config_gdoc.tasks.hourly"
# 	],
# 	"weekly": [
# 		"qcs_config_gdoc.tasks.weekly"
# 	],
# 	"monthly": [
# 		"qcs_config_gdoc.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "qcs_config_gdoc.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "qcs_config_gdoc.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "qcs_config_gdoc.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["qcs_config_gdoc.utils.before_request"]
# after_request = ["qcs_config_gdoc.utils.after_request"]

# Job Events
# ----------
# before_job = ["qcs_config_gdoc.utils.before_job"]
# after_job = ["qcs_config_gdoc.utils.after_job"]

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
# 	"qcs_config_gdoc.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


website_route_rules = [{'from_route': '/frontend/<path:app_path>', 'to_route': 'frontend'},]