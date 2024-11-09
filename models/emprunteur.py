from odoo import models, fields, api

class Emprunteur(models.Model):
    _name = 'gestion_biblio.emprunteur'
    _rec_name = 'nom'

    nom = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prénom", required=True)
    date_naissance = fields.Date(string="Date_naissance", required=True)
    state = fields.Boolean(string="State")
    sexe = fields.Selection([('homme', 'Homme'), ('femme', 'Femme')], string="Sexe")
    emprunt_id = fields.One2many('gestion_biblio.emprunt', 'emprunteur_id', string='Emprunteur')

    nbr_emprunt = fields.Integer(string='Nombre des emprunts', compute='_compute_nbr_emprunt')

    @api.depends('emprunt_id')
    def _compute_nbr_emprunt(self):
        for record in self:
            record.nbr_emprunt = len(record.emprunt_id)

    
   
