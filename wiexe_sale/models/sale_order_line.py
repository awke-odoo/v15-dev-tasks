from odoo import api, fields, models

class SaleOrderLine(models.Model):
  _inherit = 'sale.order.line'

  profit = fields.Monetary(string="Profit", compute="_compute_profit", store=True)

  @api.depends('qty_delivered', 'price_unit', 'purchase_price')
  def _compute_profit(self):
    for record in self:
      if record.invoice_status != 'invoiced':
        record.profit = record.qty_delivered * (record.price_unit - record.purchase_price)
      else:
        record.profit = record.profit