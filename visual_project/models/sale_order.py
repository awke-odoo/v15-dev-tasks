# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    photographer_id = fields.Many2one(string='Photographer', comodel_name='res.partner', readonly=False)

    # @api.depends('photographer_id')
    # def _update_purchase_orders(self):
    #     pass