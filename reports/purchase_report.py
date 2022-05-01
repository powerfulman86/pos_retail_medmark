# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

#
# Please note that these reports are not multi-currency !!!
#

from odoo import api, fields, models, tools


class PurchaseReport(models.Model):
    _inherit = "purchase.report"

    list_price = fields.Float('List Price', readonly=True)

    def _select(self):
        res = super()._select()
        # There are 3 matches
        res += ", t.list_price as list_price"
        return res

    def _group_by(self):
        res = super()._group_by()
        res += ", t.list_price"
        return res
