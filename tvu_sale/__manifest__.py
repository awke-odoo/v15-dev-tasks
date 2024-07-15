# -*- coding: utf-8 -*-
{
    'name': "tvu_sale",

    'summary': """
        TVU Networks: Auto-Cancel Expired Quotations""",

    'description': """
        Automatically cancel expired quotations to reduce administrative work.
    """,

    'author': 'awke',
    'website': 'www.odoo.com',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Custom Modules/Tech Training',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        'data/cron_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
