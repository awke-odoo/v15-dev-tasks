from odoo import api, fields, models

class ProductTemplate(models.Model):
  _inherit = 'product.template'

  price_per_case = fields.Integer(string="Price Per Case")
  price_per_pair = fields.Monetary(string="Price Per Pair")
  sales_price = fields.Monetary(compute='_compute_sales_price')

  @api.depends("price_per_case", "price_per_par")
  def _compute_sales_price(self):
    for record in self:
      record.sales_price = price_per_case * price_per_pair