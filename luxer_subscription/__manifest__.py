# -*- coding: utf-8 -*-
{
    'name': "luxer_subscription",

    'summary': """
        Luxer: Copy property from subscription to invoice delivery address""",

    'description': """
        This module keeps track of a contact record Property Partner on every subscription and copies it to the delivery address when an invoice is created.
    """,


    'author': "awke",
    'website': "www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Custom Modules/Tech Training',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_subscription'],

    # always loaded
    'data': [
        'views/sale_subscription_views.xml',
    ],
    'auto_install': True,
}
