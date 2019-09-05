# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Library(models.Model):
    _name = 'multi.company'
    _description = '图书馆'

    name = fields.Char(string="name")

    company_id = fields.Many2one('res.company', 'Company', readonly=True,
                                 default=lambda self: self.env.user.company_id, ondelete='cascade')
    user_id = fields.Many2one('res.users', string='Owner', readonly=True,
                              default=lambda self: self.env.user.id, ondelete='cascade')
    description = fields.Text(string="描述")

    @api.constrains('user_id')
    def print_log(self):
        print(self)
        print(self.__class__)
        print(self.company_id)
        print(self.env.user.company_id.id)
        print(self.user_id)
        print(self.env.user.id)
