# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from random import randint


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    lot_life_date = fields.Date(string="Expire Date", required=False, )

    def random_number(self, n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return randint(range_start, range_end)

    @api.onchange('lot_life_date')
    def set_lot_name(self):
        for ml in self:
            if ml.lot_life_date and not ml.lot_name:
                code = self.random_number(3)
                ml.lot_name = str(code) + '|' + ml.lot_life_date.strftime("%d/%m/%Y")


class ProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    def _cron_update_life_date(self):
        match = self.search([('life_date', '=', False)])
        for rec in match:
            exist_stock = self.env['stock.move.line'].search([('lot_id', '=', rec.id), ('lot_life_date', '!=', False)])
            if exist_stock:
                rec.life_date = exist_stock.lot_life_date

        match = self.search(['|', ('public_price', '=', False), ('public_price', '=', 0.0)])
        for rec in match:
            if rec.product_id.list_price > 0:
                rec.public_price = rec.product_id.list_price

    def name_get(self):
        res = []
        for lot in self:
            name = lot.name
            if lot.life_date:
                name = '[%s]- %s' % (lot.name, lot.life_date)
            res.append((lot.id, name))
        return res
