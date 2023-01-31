# -*- coding: utf-8 -*-
# from odoo import http


# class Soury(http.Controller):
#     @http.route('/soury/soury', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/soury/soury/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('soury.listing', {
#             'root': '/soury/soury',
#             'objects': http.request.env['soury.soury'].search([]),
#         })

#     @http.route('/soury/soury/objects/<model("soury.soury"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('soury.object', {
#             'object': obj
#         })
