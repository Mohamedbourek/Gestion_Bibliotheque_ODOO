# # models/article.py
from odoo import models, fields, api

class Article(models.Model):
     #_name = "gestion_biblio.article"  
     _inherit = "gestion_biblio.livre"  

     universite = fields.Char(string="Universite")
     laboratoire = fields.Char(string="Laboratoire")