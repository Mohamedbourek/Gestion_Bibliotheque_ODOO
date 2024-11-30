# -*- coding: utf-8 -*-
{
    'name' : 'gestion de bibliothéque',
    'version':'1.0',
    'category':'bibliothéque',
    'author':'bourek mohammed',
    'depends':['project','hr'],
    'description': """ ce module est déstinée pour gérer des la bibliothéque """,
   'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/hr_employee_view.xml',
        'views/article_view.xml',
        'wizard/emprunt_reset_wizard_view.xml',
        'wizard/emprunt_wizard_view.xml',
        'wizard/wizard_emprunt_ligne_view.xml',  # Ensure this line is present
        'views/menu_views.xml',
        'views/auteur.xml',
        'views/livre.xml',
        'views/emprunteur.xml',
        'views/emprunt.xml',
        'views/emprunt_ligne.xml',
        'rapport/auteur_report.xml',
        'rapport/emprunteur_report.xml',
        'rapport/emprunt_report.xml',
        'rapport/emprunt_report_extended.xml',
    ],
    'installable' : True,
    'application' : True,
    'auto_install': False,
}

