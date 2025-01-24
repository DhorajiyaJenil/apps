 frappe.ready(function() {
 	// bind events here

	frappe.web_form.after_load = () => {
 		frappe.msgprint('please fill all value carefully');
 	};
//  })
    //         console.log("hello")

    // frappe.web_form.after_load = () => {
    //     frappe.web_form.on('enable', (field, value) => {
    //         console.log("hi")
    //         frappe.msgprint('hi user');
    //     });
        
    // }

    // frappe.web_form.on('dob', (field, value) => {
    //     if(value) {
    //         dob = new Date(value);
    //         var today = new Date()
    //         var age = Math.floor((today-dob) / (365.25 * 24 * 60 * 60))

    //     }
     })