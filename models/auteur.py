from odoo import models, fields

class Auteur(models.Model):
    _name = 'gestion_biblio.auteur'
    _rec_name = 'nom'
    
    nom = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prénom", required=True)
    date_naissance = fields.Date(string="Date_naissance", required=True)
    nationalite = fields.Char(string="Nationalité", default="Algérienne")
    sexe = fields.Selection([('homme', 'Homme'), ('femme', 'Femme')], string="Sexe")
    livre_id = fields.One2many('gestion_biblio.livre', 'auteur_id', string="Livre")

