# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectTask(models.Model):
    _inherit = 'project.task'

    photographer_id = fields.Many2one(string='Photographer', comodel_name='res.partner', compute='_compute_photographer_id', inverse='_set_photographer_id', readonly=False)

    def _compute_photographer_id(self):
        for record in self:
            record.photographer_id = record.sale_order_id.photographer_id

    def _set_photographer_id(self):
        for record in self:
            record.sale_order_id.photographer_id = self.photographer_id

    @api.onchange('photographer_id')
    def _update_purchase_orders(self):
        for record in self:
            purchase_orders = record.sale_order_id._get_purchase_orders()
            for po in purchase_orders:
                po.partner_id = record.photographer_id