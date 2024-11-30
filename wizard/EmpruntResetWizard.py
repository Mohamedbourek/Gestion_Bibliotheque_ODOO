from odoo import models, fields, api

class EmpruntResetWizard(models.TransientModel):
    _name = 'gestion_biblio.emprunt.reset.wizard'
    _description = 'Assistant pour réinitialiser les emprunts'

    emprunteur_id = fields.Many2one('gestion_biblio.emprunteur', string="Emprunteur", required=True)

    def action_reset_emprunts(self):
        if self.emprunteur_id:
            self.emprunteur_id.emprunt_id.unlink()
        return {'type': 'ir.actions.act_window_close'}