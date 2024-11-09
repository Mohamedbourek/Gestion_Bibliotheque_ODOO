from odoo import models, fields, api

class Livre(models.Model):
    _name = 'gestion_biblio.livre'
    _rec_name = 'titre'

    titre = fields.Char(string="Titre", required=True)
    langue = fields.Selection([('francais', 'Français'), ('arabe', 'Arabe'), ('anglais', 'Anglais')], string="Langue")
    isbn = fields.Char(string="ISBN")
    nbr_pages = fields.Integer(string="nbre_pages")
    image_libre = fields.Char(string="Image")
    auteur_id = fields.Many2one('gestion_biblio.auteur', string="Auteur")
    emprunt_ligne_id = fields.One2many('gestion_biblio.emprunt_ligne', 'livre_id', string='Livre')
    
    @api.onchange('isbn','langue','nbr_pages','emprunt_ligne_id')
    def _onchange_livre(self):
            if self.emprunt_ligne_id:
                self.nbr_pages = self.emprunt_ligne_id.nbr_pages
                self.isbn = self.emprunt_ligne_id.isbn
                self.langue = self.emprunt_ligne_id.langue
     
   