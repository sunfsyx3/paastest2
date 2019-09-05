# -*- coding: utf-8 -*-
{
    'name': "多公司",
    'summary': "多公司",
    'description': "多公司",
    'author': "www.mypscloud.com",
    'website': 'https://www.mypscloud.com/',
    'category': 'train',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/rule.xml',
        'views/partner.xml',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
