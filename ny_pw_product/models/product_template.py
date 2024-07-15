from odoo import api, fields, models

class ProductTemplate(models.Model):
  _inherit = 'product.template'

  pair_per_case = fields.Integer(string="Pair Per Case")
  price_per_pair = fields.Monetary(string="Price Per Pair")
  list_price = fields.Monetary(string="Sales Price", 
        help="Price at which the product is sold to customers.", compute='_compute_list_price',
        store=True
      )

  @api.depends("pair_per_case", "price_per_pair")
  def _compute_list_price(self):
    for record in self:
      record.list_price = record.pair_per_case * record.price_per_pair