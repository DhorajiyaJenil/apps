// Copyright (c) 2024, D-codE and contributors
// For license information, please see license.txt

 frappe.ui.form.on("client side", {
 	refresh(frm) {
       // frm.set_intro('Now you can create a new client side doctype')

       if(frm.is_new()){
            frm.set_intro('Now you can create a new client side doctype')
       }
 	}
 });
