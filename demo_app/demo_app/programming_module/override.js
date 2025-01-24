// override.js

// Override the 'refresh' event for the 'Second' form
frappe.ui.form.on('Second', {
    refresh: function(frm) {
        // Custom logic when the 'Second' form is refreshed
        
        // Example: Log a message to the console
        console.log("Second form refreshed");
        
        // Example: Add a custom button to the form
        frm.add_custom_button(__('My Custom Button'), function() {
            frappe.msgprint(__('You clicked the custom button on Second form!'));
        });

        // Example: Dynamically change a field's label
        frm.set_df_property('fieldname', 'label', 'Updated Field Label');
    },

    // Override the 'validate' event for custom validation
    validate: function(frm) {
        // Custom validation logic
        console.log("Custom validation logic for Second form");

        // Example: Prevent saving if a specific field is empty
        if (!frm.doc.fieldname) {
            frappe.msgprint(__('Please fill in the required field.'));
            frappe.validated = false;  // Prevent form submission
        }
    },

    // Override other events as needed (e.g., on change of a field)
    fieldname_onchange: function(frm) {
        // Custom logic on field change
        console.log("Field 'fieldname' changed in Second form");
    }
});
