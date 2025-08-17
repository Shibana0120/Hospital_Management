

from odoo import models, fields, api,_


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'This is patient form'

    patient_num = fields.Char(string="Patient No.", required=True, copy=False, readonly=True,
                               index=True, default=lambda self: _('New'))
    name = fields.Char(String = 'Name',required = True)
    age= fields.Integer('Age')
    notes = fields.Text(String='Notes')
    adm_date = fields.Date(String='AdmittedDate')
    image = fields.Binary(String='image')
    description = fields.Text(String='desc')
    doctor = fields.Many2one('hospital.doctor')

    s_field = fields.Selection([('Draft', 'Draft'), ('Confirm', 'Confirm'), ('Done', 'Done')], default='Draft')

    def action_confirm(self):
        for x in self:
            x.s_field = 'Confirm'

    def action_done(self):
        for x in self:
            x.s_field = 'Done'

    @api.model
    def create(self, vals):
        if vals.get('patient_num', _('New')) == _('New'):
            vals['patient_num'] = self.env['ir.sequence'].next_by_code('patient.no.sequence') or _('New')
        result = super(HospitalPatient, self).create(vals)
        return result


