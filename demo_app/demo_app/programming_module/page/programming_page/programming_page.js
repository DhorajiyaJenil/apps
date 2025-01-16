frappe.pages['programming-page'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Demo Page',
		single_column: true
	});


	page.set_title('My Page')

	page.set_indicator('Done', 'green')

	let $btn = page.set_primary_action('New', () =>frappe.msgprint("clicked New"),'octicon oction-plus')

	let $btnone = page.set_secondary_action('Refresh', () => frappe.msgprint("clicked Refresh"),'oction oction-plus')

	page.add_menu_item('send Email', () => frappe.msgprint("clicked send Email"))
	
	page.add_action_item('Delete', () => frappe.msgprint("clicked Delete"))

	let field = page.add_field({
		label: 'Status',
		fieldtype: 'Select',
		fieldname: 'Status',
		options: [
			'Open',
			'Closed',
			'Cancelled'
		],
		Change() {
			frappe.msgprint(field.get_value());
		}
	})
}

	//$(frappe.render_template("programming_page", {})).appendTo(page.body);

// 	$(frappe.render_template("programming_page",{
// 		data:"hi frappe"
// 	})).appendTo(page.body);

// }