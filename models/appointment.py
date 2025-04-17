from odoo import api, fields, models, _
from datetime import datetime
from datetime import date


class Appointment(models.Model):
    _name = 'hospital.appointment'
    _rec_name = 'patient_id'
    _description = 'Hospital Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'app_seq desc'

    # sequence generate field
    app_seq = fields.Char(
        string="Appointment Id",
        required=True, copy=False, readonly=False,
        index='trigram',
        default=lambda self: _('New'))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('app_seq', _("New")) == _("New"):
                vals['app_seq'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _("New")
        return super(Appointment, self).create(vals_list)


    patient_id = fields.Many2one('hospital.patient', string='Patient', tracking=True)
    gender = fields.Selection(string="Gender", selection=[('male', 'Male'), ('female', 'Female'),],related='patient_id.gender')
    appointment_date = fields.Date(string='Appointment Date', default=date.today(), tracking=True)
    booking_date = fields.Datetime(string='Booking Date', default=datetime.now(), tracking=True)
    doctor_id = fields.Many2one('res.users', string='Doctor')

    # state field
    state = fields.Selection([
        ('draft', 'Draft'),
        ('process', 'In Progress'),
        ('confirm', 'Confirmed'),
        ('canceled', 'Cancelled')
    ], 'Status', readonly=True, copy=False, default='draft', required=True, tracking=True)


    # button action
    def action_draft(self):
        self.state = 'draft'


    def action_process(self):
        self.state = 'process'

    def action_confirm(self):
        self.state = 'confirm'

    def action_cancel(self):
        self.state = 'canceled'
