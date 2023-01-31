# -*- coding: utf-8 -*-
# from odoo import http


# class PisteModule(http.Controller):
#     @http.route('/piste_module/piste_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/piste_module/piste_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('piste_module.listing', {
#             'root': '/piste_module/piste_module',
#             'objects': http.request.env['piste_module.piste_module'].search([]),
#         })

#     @http.route('/piste_module/piste_module/objects/<model("piste_module.piste_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('piste_module.object', {
#             'object': obj
#         })
