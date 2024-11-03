from odoo import models, fields

class Livre(models.Model):
    _name = 'gestion_biblio.livre'
    _rec_name = 'titre'

    titre = fields.Char(string="Titre", required=True)
    langue = fields.Selection([('francais', 'Français'), ('arabe', 'Arabe'), ('anglais', 'Anglais')], string="Langue")
    isbn = fields.Char(string="ISBN")
    nbr_pages = fields.Integer(string="nbre_pages")
    image_libre = fields.Char(string="Image")
    auteur_id = fields.Many2one('gestion_biblio.auteur', string="Auteur")
   