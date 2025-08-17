from odoo import models, fields, api


class HospitalNurse(models.Model):
    _name = 'hospital.nurse'
    _description = 'hospital nurse list'

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    DOB= fields.Char(string = 'DOB')
    image = fields.Binary(string="Image")
    gender=fields.Text(string="Gender")
    contact_number = fields.Integer("Contact_Number")
    email = fields.Char(string="Email")
    address = fields.Text(string="Address")