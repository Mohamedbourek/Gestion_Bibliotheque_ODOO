from odoo import models, fields

class EmpruntLigne(models.Model):
    _name = 'gestion_biblio.emprunt_ligne'
    isbn = fields.Char(string="ISBN")
    nbr_pages = fields.Integer(string="nbre_pages")
    langue = fields.Selection([('francais', 'Français'), ('arabe', 'Arabe'), ('anglais', 'Anglais')], string="Langue")
    
    livre_id = fields.Many2one('gestion_biblio.livre', string='Emprunt')
    emprunt_id = fields.Many2one('gestion_biblio.emprunt', string='Livre')