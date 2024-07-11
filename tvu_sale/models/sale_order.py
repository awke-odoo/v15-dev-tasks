from datetime import datetime

from odoo import models


class SaleOrder(models.Model):
  _inherit = 'sale.order'

  def _check_expiration_date(self):
    for quote in self.env['sale.order'].search([('state','!=','cancel'), ('state', '!=', 'done')]):
        if quote.validity_date:
          if quote.validity_date < datetime.now().date():
            quote.write({'state': 'cancel'})