from odoo import models, fields, api

class EmpruntLigne(models.Model):
    _name = 'gestion_biblio.emprunt_ligne'
    isbn = fields.Char(string="ISBN")
    nbr_pages = fields.Integer(string="nbre_pages")
    langue = fields.Selection([('francais', 'Français'), ('arabe', 'Arabe'), ('anglais', 'Anglais')], string="Langue")
    
    livre_id = fields.Many2one('gestion_biblio.livre', string='Livre')
    emprunt_id = fields.Many2one('gestion_biblio.emprunt', string='Emprunt')

    @api.onchange('livre_id')
    def _onchange_livre_id(self):
        if self.livre_id:
            self.isbn = self.livre_id.isbn
            self.langue = self.livre_id.langue
            self.nbr_pages = self.livre_id.nbr_pages