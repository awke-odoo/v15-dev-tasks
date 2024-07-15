# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'matrix_product',
    'version': '0.1',
    'category': 'Custom Modules/Tech Training',
    'depends': ['product'],
    'description': """
This is an extended module for managing products for NY P&W Shoes in Odoo.
    """,
    'license': 'OPL-1',
    'author': 'awke',
    'website': 'www.odoo.com',
    'data': [
      'data/product_template_data.xml',
      'views/product_template_views.xml',
    ],
    'demo': [],
    'auto_install': True,
}