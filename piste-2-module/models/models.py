# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class piste-2-module(models.Model):
#     _name = 'piste-2-module.piste-2-module'
#     _description = 'piste-2-module.piste-2-module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
