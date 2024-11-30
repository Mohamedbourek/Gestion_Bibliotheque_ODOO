from odoo import models, fields, api

class EmpruntWizard(models.TransientModel):
    _name = 'gestion_biblio.emprunt_wizard'
    _description = 'Assistant pour ajouter un emprunt'

    emprunteur_id = fields.Many2one('gestion_biblio.emprunteur', string="Emprunteur", required=True)
    emprunt_id = fields.Many2one('gestion_biblio.emprunt', string="Emprunt", required=True, ondelete='cascade')
    date_fin = fields.Date(string="Date de fin", required=True)

    def action_ajouter_emprunt(self):
        emprunt_lignes = []
        for emprunt_ligne in self.emprunt_id:
            emprunt_lignes.append((0, 0, {'livre_id': emprunt_ligne.id}))
        
        emprunt_vals = {
            'emprunteur_id': self.emprunteur_id.id,
            'date_debut': fields.Date.today(),
            'date_fin': self.date_fin,
            'rendu': 'non',
            'ligne_emprunt_ids': [(6, 0, emprunt_lignes)],
        }
        self.env['tp_erp.emprunt'].create(emprunt_vals)
        return {'type': 'ir.actions.act_window_close'}
        def launch_emprunt_ligne_wizard(self):
            return {
                'name': 'Ajouter des livres',
                'type': 'ir.actions.act_window',
                'res_model': 'gestion_biblio.emprunt_ligne_wizard',
                'view_mode': 'form',
                'target': 'new',
                'context': {'default_emprunt_id': self.id}
            }