from odoo import models, fields , api

class Emprunt(models.Model):
    _name = 'gestion_biblio.emprunt'
    
    date_debut = fields.Date(string="Date début", required=True)
    date_fin = fields.Date(string="Date fin", required=True)
    rendu = fields.Selection([('oui', 'Oui'), ('non', 'Non')], string="Rendu")
    emprunteur_id = fields.Many2one('gestion_biblio.emprunteur', string="Emprunteur")
    emprunt_ligne_id = fields.Many2one('gestion_biblio.emprunt_ligne', string="EmpruntLigne")


    

