# -*- coding: utf-8 -*-
{
    'name': "Print Invoice using 'Professional Invoice Templates' in POS",
    'support': 'support@optima.co.ke',

    'summary': """
        If you already purchased our 'customized_invoice' and you want to print invoice from POS using the templates, then this module will help you""",

    'description': """
    If you already purchased our 'customized_invoice' and you want to print invoice from POS using the templates, then this module will help you
    """,

    'author': "Optima ICT Services LTD",
    'website': "http://www.optima.co.ke",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Point Of Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
