from odoo import models, fields

class Emprunteur(models.Model):
    _name = 'gestion_biblio.emprunteur'
    _rec_name = 'nom'

    nom = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prénom", required=True)
    date_naissance = fields.Date(string="Date_naissance", required=True)
    state = fields.Boolean(string="State")
    sexe = fields.Selection([('homme', 'Homme'), ('femme', 'Femme')], string="Sexe")
    emprunt_id = fields.One2many('gestion_biblio.emprunt', 'emprunteur_id', string='Emprunteur')