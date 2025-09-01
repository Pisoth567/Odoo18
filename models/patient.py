from tokenize import String
from odoo import api, fields, models
class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Hospital Patient'


    name = fields.Char(string="Name", tracking=True)
    ref = fields.Char(string="Reference")
    age = fields.Integer(string="Age", tracking=True)
    Gender = fields.Selection([('male', 'Male'), ('female','Female')], string="Gender", tracking=True)
    address = fields.Text()
    active = fields.Boolean(String="Active", default=True)