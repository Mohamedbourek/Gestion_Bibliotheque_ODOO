# -*- coding: utf-8 -*-
{
    'name' : 'gestion de bibliothéque',
    'version':'1.0',
    'category':'bibliothéque',
    'author':'bourek mohammed',
    'depends':['project'],
    'description': """ ce module est déstinée pour gérer des la bibliothéque """,
   'data': [
        'security/ir.model.access.csv',
        'views/auteur.xml',
        'views/livre.xml',
        'views/emprunteur.xml',
        'views/emprunt.xml',
        'views/emprunt_ligne.xml',
        'views/menu_views.xml'
    ],
    'installable' : True,
    'application' : True,
    'auto_install': False,
}

