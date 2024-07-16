# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleSubscription(models.Model):
    _inherit = 'sale.subscription'

    property_partner_id = fields.Many2one(comodel_name='res.partner', string='Property Partner')

    def _prepare_invoice_data(self):
        res = super()._prepare_invoice_data()
        if self.property_partner_id:
            res['partner_shipping_id'] = self.property_partner_id.id
        return res
