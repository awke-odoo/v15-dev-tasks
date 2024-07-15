# -*- coding: utf-8 -*-
{
    'name': "visual_project",

    'summary': """
        Visual Properties: Updating Vendor on P.O. when changed on task and S.O.""",

    'description': """
        When the 'Photographer' assigned on the Sale Order and Task is changed, the RFQ/Purchase Order (Vendor) is also changed/updated with the same 'Photographer'.
    """,

    'author': "awke",
    'website': "www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Custom Modules/Tech Training',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_project', 'sale_management', 'purchase', 'contacts'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/project_task_views.xml',
    ],
}
