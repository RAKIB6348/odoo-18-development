from odoo import api, fields, models
from datetime import datetime


class Patient(models.Model):
    _name = 'hospital.patient'
    _rec_name = 'name'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']



    image = fields.Binary(string='Image')
    name = fields.Char(string='Name', required=True)
    register_date = fields.Datetime(string='Register Date', default=datetime.now())
    age = fields.Integer(string='Age')
    gender = fields.Selection(string="Gender", selection=[('male', 'Male'), ('female', 'Female'), ], required=True, )
    phone = fields.Char(string='Phone')