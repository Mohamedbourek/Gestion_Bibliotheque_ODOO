from odoo import models, fields, api

class Emprunt(models.Model):
    _name = 'gestion_biblio.emprunt'
    
    date_debut = fields.Date(string="Date début", required=True,default=fields.Date.today, readonly=True)
    date_fin = fields.Date(string="Date fin", required=True)
    rendu = fields.Selection([('oui', 'Oui'), ('non', 'Non')], string="Rendu")

    emprunteur_id = fields.Many2one('gestion_biblio.emprunteur', string="Emprunteur")
    emprunt_ligne_id = fields.One2many('gestion_biblio.emprunt_ligne', 'emprunt_id', string="EmpruntLigne")

    @api.onchange('date_fin')
    def _onchange_date_fin(self):
        if self.date_fin and self.date_fin == fields.Date.today():
            self.rendu = 'oui'
        else:
            self.rendu = 'non' 
            
    @api.constrains('date_fin', 'date_debut')
    def _check_date_fin(self):
        for record in self:
            if record.date_fin < record.date_debut:
                raise ValidationError("La date de fin ne peut pas être antérieure à la date de début.")


