from odoo import api, fields, models


class Patient(models.Model):
    _name = 'hospital.patient'
    _rec_name = 'name'
    _description = 'Hospital Patient'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection(string="Gender", selection=[('male', 'Male'), ('female', 'Female'), ], required=True, )
