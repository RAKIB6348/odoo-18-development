from odoo import api, fields, models, _
from datetime import datetime


class Patient(models.Model):
    _name = 'hospital.patient'
    _rec_name = 'name'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'pat_seq desc'
    _rec_names_search = ['name','pat_seq']



    image = fields.Binary(string='Image')
    name = fields.Char(string='Name', required=True, tracking=True)
    register_date = fields.Datetime(string='Checkup Date', default=datetime.now(), tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection(string="Gender", selection=[('male', 'Male'), ('female', 'Female'), ], required=True,tracking=True )
    phone = fields.Char(string='Phone', tracking=True)
    doctor_id = fields.Many2one('res.users', string='Doctor', tracking=True)
    ref = fields.Char(string='Reference', tracking=True)
    tag_ids = fields.Many2many('patient.tag', string='Tag')


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
                vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient.ref')
        return super(Patient, self).create(vals_list)
    
    # write method
    def write(self, vals):
        if not self.ref:
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient.ref')
        return super(Patient, self).write(vals)


    # copy method
    def copy_data(self, default=None):
        if default is None:
            default = {}
        if not default.get('name'):
            default['name'] = self.name + "(copy)"
        return super(Patient, self).copy_data(default)
