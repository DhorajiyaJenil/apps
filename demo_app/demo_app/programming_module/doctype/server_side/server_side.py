# Copyright (c) 2024, D-codE and contributors
# For license information, please see license.txt

#  import frappe
#  from frappe import _
#  from frappe.model.document import Document

#  class serverside(Document):
# 	pass
# 	@frappe.whitelist()
# 	def frm_call(self,msg):
# 		import time
# 		time.sleep(5)
# 		#frappe.msgprint(msg)

# 		self.age = 78


	  #	return "hi this message from frm_call"


	

	#frappe.db.get_list(doctype, filters, or_filters, fields, order_by, group_by, start, page_length)

		# def validate(self):
		# 	self.get_list()

		# def get_list(self):
		# 	doc = frappe.db.get_list('client side',
		# 	filters={
		# 		'enable' : 1
		# 	},
		# 	fields=['first_name','age']
		# 	)
			
		# 	for d in doc:
		# 		frappe.msgprint(_("The Parent first name is {0} and age is {1}").format(d.first_name,d.age))

	

	# def validate(self):
	# 	self.get_document()

	# def get_document(self):
	# 	doc = frappe.get_doc('client side', self.client_side_doc)
	# 	frappe.msgprint(_("The first name is {0} and age is {1}").format(doc.first_name,doc.age))


	# def validate(self):
	# 	frappe.msgprint(_("hello my full name is '{0}' ").format(
	# 		self.first_name +" "+ self.middle_name+" "+self.last_name))
		

	#   def validate(self):
	# 	  for row in self.get("family_member"):
	# 		  frappe.msgprint(_(
	#  			  "{0}. The family member name is '{1}' and relation is '{2}'").format(
	# 			  row.idx,row.name1,row.relation
	#  			)
	# 		)


	#delete doc()

	#frappe.delete_doc(doctype, name)

		# def validate(self):
		# 	frappe.delete_doc('client side','PR-0009')

	#doc.insert()

		# def validate(self):
		# 	self.new_document()

		# def new_document(self):
		# 	doc = frappe.new_doc('client side')
		# 	doc.first_name = 'job'
		# 	doc.age = '23'
		# 	doc.insert()

	#doc.save()

		# def validate(self):
		# 	self.new_document()

		# def save_document(self):
		# 	doc = frappe.save_doc('client side')
		# 	doc.first_name = 'job'
		# 	doc.age = '34'
		# 	doc.save()









# class serverside(Document):
	
# 	def validate(self):
# 		self.new_document()

# 	def new_document(self):
# 		doc = frappe.new_doc('client side')
# 		doc.first_name = 'jenil'
# 		doc.last_name = 'jay'
# 		doc.age = 13

# 		doc.insert()
