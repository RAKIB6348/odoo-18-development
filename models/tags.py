from odoo import fields, models


class Tags(models.Model):
    _name = 'patient.tag'
    _description = 'Patient Tag'


    name = fields.Char(string='Name', required=True)
    color = fields.Integer(string='Color')