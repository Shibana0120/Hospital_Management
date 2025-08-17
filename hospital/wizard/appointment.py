from odoo import api, fields, models

class AppointmentWizard(models.TransientModel):
    _name = "hospital.appointment"
    _description = "Appointment Wizard"

    start_date = fields.Date(string="Date From")
    end_date = fields.Date(string="Date To")

    def Excel_report(self):
        appointments = self.env['hospital.patient'].search_read([
            ('adm_date', '>=', self.start_date), ('adm_date', '<=', self.end_date)])
        print("appointments", appointments)
        val = {
            'appointments': appointments,
            'start_d': self.start_date,
            'end_d': self.end_date
        }
        return self.env.ref('hospital.action_xls_appointment').report_action(self, data=val)

    def Pdf_report(self):
        print("hai")
        store1 = {
            'ids': self.ids,
            'model': self._name,
            'form': {'start_d': self.start_date,
                     'end_d': self.end_date,
                     }, }
        return self.env.ref('school.admission_pdf').report_action(self, data=store1)
