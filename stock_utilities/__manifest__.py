# -*- coding: utf-8 -*-
# Copyright (c) 2017 Alfredo de la fuente <alfredodelafuente@avanzosc.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Stock Utilities',
    'version': '11.0.1.0.0',
    'license': "AGPL-3",
    'summary': '''Stock utilities''',
    'author':  "AvanzOSC",
    'website': 'http://www.avanzosc.es',
    'contributors': [
        "Ana Juaristi <anajuaristi@avanzosc.es>",
        "Alfredo de la Fuente <alfredodelafuente@avanzosc.es",
    ],
    'category': 'Warehouse Management',
    'depends': [
        'stock',
    ],
    'data': [
        'views/product_view.xml',
        'views/stock_picking_view.xml',
        'views/stock_move_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
