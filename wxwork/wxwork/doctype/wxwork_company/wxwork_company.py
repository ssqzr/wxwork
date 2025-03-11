# Copyright (c) 2025, ssqzr and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class WXWorkCompany(Document):
	def validate(self):
		self.company_name = self.company_name.strip()
		self.company_id = self.company_id.strip()
