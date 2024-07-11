# -*- coding: utf-8 -*-
{
    'name': "wiexe_sale",

    'summary': """
        Wiexe Digital : SO list view computed field""",

    'description': """
        Create a computed field to view profit and make it read-only after it is created.
    """,

    "author": "Odoo Inc",
    "website": "www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Custom Modules/Tech Training',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_margin'],

    # always loaded
    'data': [
      'views/sale_order_line_menuitems.xml',
      'views/sale_order_line_views.xml',
    ],
    'demo': [],
    'auto_install': True,
}
