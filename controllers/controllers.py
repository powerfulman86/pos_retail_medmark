# -*- coding: utf-8 -*-
# from odoo import http


# class PosRetailMedmark(http.Controller):
#     @http.route('/pos_retail_medmark/pos_retail_medmark/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_retail_medmark/pos_retail_medmark/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_retail_medmark.listing', {
#             'root': '/pos_retail_medmark/pos_retail_medmark',
#             'objects': http.request.env['pos_retail_medmark.pos_retail_medmark'].search([]),
#         })

#     @http.route('/pos_retail_medmark/pos_retail_medmark/objects/<model("pos_retail_medmark.pos_retail_medmark"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_retail_medmark.object', {
#             'object': obj
#         })
