// Copyright (c) 2025, D-codE and contributors
// For license information, please see license.txt

frappe.ui.form.on("Property", {
    setup: function(frm) {
        frm.check_amenities_duplicate = function(frm, row) {
            frm.doc.amenities.forEach(item => {
                if (row.amenity == '' || row.idx) {
                    // pass
                } else {
                    if (row.amenity == item.amenity) {
                        row.amenity = '';
                        frappe.throw(_(`${item.amenity} already exists in row ${item.idx}`));
                        frm.refresh_field('amenities');
                    }
                }
            });
        };

        frm.check_flat_against_outdoor_kitchen = function(frm, row) {
            if (row.amenity == "Outdoor_Kitchen" && frm.doc.property_type == "Flat") {
                let amenity = row.amenity;
                row.amenity = '';
                frappe.throw(_(`${amenity} cannot exist in a flat`));
                frm.refresh_field('amenities');
            }
        };
    },
    refresh: function(frm) {
        // say hi
        frm.add_custom_button('Say Hi', () => {
            frappe.prompt('Address', ({ value }) => {
                if (value) {
                    frm.set_value('address', value);
                    frm.refresh_field('address');
                    frappe.msgprint(_('Address field updated with ${value}'));
                }
            });
        }, "Actions");

        // check property types
        frm.add_custom_button('Check Property Types', () => {
            let property_type = frm.doc.property_type;
            console.log(property_type);
        }, "Actions");
    },
});

frappe.ui.form.on('Property Amenity Detail', {
    amenity: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        console.log(row);
    }
});
