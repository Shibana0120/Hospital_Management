
from odoo import models, fields, api


class hospitalAppointmentXlsx(models.AbstractModel):
    _name = 'report.hospital.report_appointment_xlsx'
    _inherit = 'report.report_xlsx.abstract'



    def generate_xlsx_report(self,workbook,data,mod):
        format1 = workbook.add_format({'font_size': 14, 'align': 'vcenter', 'bold': True,   'border': 1,
                                        'border_color': 'green'})
        format2 = workbook.add_format({'font_size': 10, 'align': 'vcenter', 'border': 1,'border_color': 'green'
                                       })


        sheet = workbook.add_worksheet("Patient Details")
        bold = workbook.add_format({'bold': True})
        row = 3
        col = 3
        sheet.merge_range('C2:D2', data['start_d'])
        sheet.merge_range('C3:D3', data['end_d'])

        sheet.write(row, col, ' Name', format1)
        sheet.write(row, col + 1, ' Age', format1)
        sheet.write(row, col + 2, 'Admit Date', format1)
        # sheet.write(row, col + 3, 'Doctor', bold)
        sheet.write(row, col + 4, 'Notes', format1)

        for x in data['appointments']:
            row += 1
            sheet.write(row, col, x['name'],format2)
            sheet.write(row, col + 1, x['adm_date'],format2)
            sheet.write(row, col + 2, x['age'],format2)
            # sheet.write(row,col + 3,x['doctor']format2)
            sheet.write(row,col + 4, x['notes'],format2)