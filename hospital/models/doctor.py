from odoo import models, fields, api


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'hospital doctor list'
    _rec_name = 'doct_name'

    doct_name = fields.Char(string='Name', required=True)
    doct_age = fields.Integer('Age')
    image = fields.Binary(string="image")
    spc = fields.Text(string="specialization")

    user_id = fields.Many2one('res.users', string='Related User')