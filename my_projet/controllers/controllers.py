# -*- coding: utf-8 -*-
from odoo import http


class MyProjet(http.Controller):
    @http.route('/my_projet/my_projet', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/my_projet/my_projet/objects', auth='public')
    def list(self, **kw):
        return http.request.render('my_projet.listing', {
            'root': '/my_projet/my_projet',
            'objects': http.request.env['my_projet.my_projet'].search([]),
        })

    @http.route('/my_projet/my_projet/objects/<model("my_projet.my_projet"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('my_projet.object', {
            'object': obj
        })
