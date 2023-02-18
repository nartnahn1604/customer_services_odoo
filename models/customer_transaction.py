from odoo import models, fields, api
class CustomerTransaction(models.Model):
    _name = 'customer.transaction'
    date_time = fields.Datetime('Time')
    contents = fields.Char('Content')
    state = fields.Selection([('green', 'Green'), ('red', 'Red'), ('gray', 'Gray')], readonly=True, default='gray')