frappe.ui.form.on('Customer', {
    refresh: function(frm) {
        // Hide the "Actions" dropdown button in the menu
        $('.btn[aria-expanded="false"][data-toggle="dropdown"]').each(function() {
            if ($(this).text().trim() === "Actions") {
                $(this).hide();
            }
        });
    }
});
