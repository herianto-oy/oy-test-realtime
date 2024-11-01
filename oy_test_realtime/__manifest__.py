# -*- coding: utf-8 -*-
{
    'name': "oy_test_realtime",
    'summary': "RnD Realtime",
    'description': """
        Long description of module's purpose
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'hr'],
    'data': [
        'views/views.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'oy_test_realtime/static/src/js/oy_realtime_action.xml',
            'oy_test_realtime/static/src/js/oy_realtime_action.js',
        ]
    },
}

