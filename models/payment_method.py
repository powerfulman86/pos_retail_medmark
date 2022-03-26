# -*- coding: utf-8 -*-


from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError


class PosPaymentMethod(models.Model):
    _inherit = "pos.payment.method"

    payment_commission = fields.Boolean(string="Commission", default=False)
    commission_account_id = fields.Many2one('account.account', string='Commission Account', ondelete='restrict',
                                            help='Commission Account.')
    commission_type = fields.Selection(string="Commission Type", default='fixed',
                                       selection=[('fixed', 'Fixed'), ('percent', 'Percentage'), ], required=False, )
    commission_value = fields.Integer(string="Commission Value", required=False, )
    commission_percent = fields.Integer(string="Commission Percent", required=False, )

    is_payment_reference = fields.Boolean(string="Payment Ref. Required", default=False)

    @api.onchange('is_cash_count')
    def _change_cash(self):
        if self.is_cash_count:
            self.is_payment_reference = False

    @api.onchange('payment_commission')
    def _onchange_payment_commission(self):
        if not self.payment_commission:
            self.commission_account_id = False
            self.commission_value = False
            self.commission_percent = False
