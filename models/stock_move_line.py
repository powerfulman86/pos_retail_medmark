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

    # def _action_done(self):
    #     super(StockMoveLine, self)._action_done()
    #     for rec in self:
    #         exist_lot = self.env['stock.production.lot'].search([('id', '=', rec.lot_id.id)])
    #         if exist_lot and rec.lot_life_date:
    #             exist_lot.life_date = rec.lot_life_date


class ProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    def name_get(self):
        res = []
        for lot in self:
            name = lot.name
            if lot.life_date:
                name = '[%s]- %s' % (lot.name, lot.life_date)
            res.append((lot.id, name))
        return res

    # @api.model
    # def create(self, vals):
    #     lot = super(ProductionLot, self).create(vals)
    #
    #     exist_lot = self.env['stock.move.line'].search([('lot_id', '=', lot.id)])
    #     if exist_lot and exist_lot.lot_life_date:
    #         self.life_date = exist_lot.lot_life_date
