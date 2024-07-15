from odoo import api, fields, models

class ProductTemplate(models.Model):
  _inherit = 'product.template'

  product_group = fields.Selection(string="Product Group", selection=[
    ('year', 'Year'),
    ('meal', 'Meal'),
    ('king', 'King'),
    ('user', 'User')
  ], readonly=False, default='user'
  )
  barcode = fields.Char('Barcode', compute='_compute_barcode', inverse='_set_barcode', search='_search_barcode')

  @api.depends('product_group')
  def _compute_barcode(self):
    for record in self:
      record.barcode = record.product_group[:2].upper()
      record.barcode += self.env['ir.sequence'].next_by_code('barcode')