# -*- coding: utf-8 -*-
{
    'name': "Pos Retail Medmark",
    'summary': """POS Retail MedMark custom """,
    'description': """POS MedMark custom """,
    'author': "",
    'category': 'Uncategorized',
    'version': '13.0.0.1',
    'depends': ['base', 'point_of_sale', 'pos_retail'],

    # always loaded
    'data': [
        'views/pos_session.xml',
    ],
    'qweb': [

    ],
    'images': ['static/description/icon.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
