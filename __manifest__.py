# -*- coding: utf-8 -*-
{
    'name':'Pokedex',
    'version': '0.1',
    'category': 'Dev',
    'summary': 'Curso Oddo',
    'description': """
Curso desarrollo Addo (Pokedex)
===============================
RST
    """,
    'depends': [
        'contacts',
    ],
    'data': [
       'security/ir.model.access.csv',
       'views/pokemon_views.xml' ,
       'views/res_partner_views.xml',
       'wizard/pokemon_evolve_view.xml'
    ],
    'installable': True,
    'auto_install': False,
}