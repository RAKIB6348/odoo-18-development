from odoo import api, fields, models, _
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


    # sequence generate field
    pat_seq = fields.Char(
        string="Patient Id",
        required=True, copy=False, readonly=False,
        index='trigram',
        default=lambda self: _('New'))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('pat_seq', _("New")) == _("New"):
                vals['pat_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _("New")
        return super(Patient, self).create(vals_list)