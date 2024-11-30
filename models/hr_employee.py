# models/hr_employee.py
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
 
class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'
 
    date_debut = fields.Date(string="Date de début")
    nombre_annee = fields.Integer(string="Nombre d'années d'expérience", compute='_compute_nombre_annee', store=True)
    num_retraite = fields.Char(string="Numéro de retraite") 
    date_retraite = fields.Date(string="Date de retraite")
 
    @api.depends('date_debut')
    def _compute_nombre_annee(self):
        for employee in self:
            if employee.date_debut:
                today = fields.Date.today()
                delta = relativedelta(today, employee.date_debut)
                employee.nombre_annee = delta.years
            else:
                employee.nombre_annee = 0