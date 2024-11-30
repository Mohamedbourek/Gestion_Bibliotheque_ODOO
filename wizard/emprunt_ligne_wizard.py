from odoo import models, fields

class EmpruntLigneWizard(models.TransientModel):
    _name = 'gestion_biblio.emprunt_ligne_wizard'
    _description = 'Assistant pour ajouter une ligne d\'emprunt'
    emprunt_id = fields.Many2one('gestion_biblio.emprunt', string="Emprunt", required=True, ondelete='cascade')
    livre_id = fields.Many2one('gestion_biblio.livre', string="Livre", required=True)
    isbn = fields.Char(related='livre_id.isbn', string='ISBN', readonly=True)
    nbr_pages = fields.Integer(related='livre_id.nbr_pages', string="Nombre de Pages", readonly=True)
    langue = fields.Selection(related='livre_id.langue', string="Langue du Livre", readonly=True)

    def action_ajouter_ligne_emprunt(self):
        emprunt_vals = {
            'emprunt_id': self.emprunt_id.id,
            'livre_id': self.livre_id.id,
            'emprunt_id': self.emprunt_id.id,
            'livre_id': self.livre_id.id,
        }
        self.env['gestion_biblio.emprunt_ligne'].create(emprunt_vals)
        return {'type': 'ir.actions.act_window_close'}

