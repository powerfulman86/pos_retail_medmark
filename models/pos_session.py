# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError


class PosSession(models.Model):
    _inherit = "pos.session"

    ended = fields.Boolean('ended', compute="compute_end")

    @api.depends('cash_register_balance_end_real')
    def compute_end(self):
        for rec in self:
            rec.ended = False
            if (rec.cash_register_balance_end_real > 0 and rec.state != 'closed') or self.env.user.has_group(
                    'point_of_sale.group_pos_manager'):
                rec.ended = True
            # if self.env.user.has_group('point_of_sale.group_pos_manager'):
            #     rec.ended = False

    def print_z_report(self):
        if self.ended is not True:
            raise ValidationError(_("Please Set Closing Cash Before Print !"))

        datas = {
            'ids': self._ids,
            'form': self.read()[0],
            'model': 'pos.sale.report'
        }
        datas['form']['session_ids'] = self.id
        return self.env.ref('pos_retail.report_pos_sales_pdf').report_action(self, data=datas)
