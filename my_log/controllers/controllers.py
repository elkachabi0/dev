# -*- coding: utf-8 -*-
# from odoo import http


# class MyLog(http.Controller):
#     @http.route('/my_log/my_log', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_log/my_log/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_log.listing', {
#             'root': '/my_log/my_log',
#             'objects': http.request.env['my_log.my_log'].search([]),
#         })

#     @http.route('/my_log/my_log/objects/<model("my_log.my_log"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_log.object', {
#             'object': obj
#         })
