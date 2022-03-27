# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    lot_life_date = fields.Date(string="Expire Date", required=False, )

    @api.onchange('lot_life_date')
    def set_lot_name(self):
        for ml in self:
            if ml.lot_life_date and not ml.lot_name:
                ml.lot_name = ml.lot_life_date.strftime("%d/%m/%Y")


class ProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    def _cron_update_life_date(self):
        match = self.search([('life_date', '=', False)])
        for rec in match:
            exist_stock = self.env['stock.move.line'].search([('lot_id', '=', rec.id), ('lot_life_date', '!=', False)])
            if exist_stock:
                rec.life_date = exist_stock.lot_life_date

    def name_get(self):
        res = []
        for lot in self:
            name = lot.name
            if lot.life_date:
                name = '[%s]- %s' % (lot.name, lot.life_date)
            res.append((lot.id, name))
        return res
