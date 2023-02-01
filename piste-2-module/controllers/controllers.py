# -*- coding: utf-8 -*-
# from odoo import http


# class Piste-2-module(http.Controller):
#     @http.route('/piste-2-module/piste-2-module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/piste-2-module/piste-2-module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('piste-2-module.listing', {
#             'root': '/piste-2-module/piste-2-module',
#             'objects': http.request.env['piste-2-module.piste-2-module'].search([]),
#         })

#     @http.route('/piste-2-module/piste-2-module/objects/<model("piste-2-module.piste-2-module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('piste-2-module.object', {
#             'object': obj
#         })
