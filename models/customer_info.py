from email.policy import default
import re
from odoo import models, fields, api
from odoo.exceptions import ValidationError
class CustomerInfo (models.Model):
    _name = 'customer.info'
    name = fields.Char('Name', required=True)
    phone_number = fields.Char('Phone', size = 10, required=True)
    email = fields.Char('Email', required=True)
    address = fields.Char('Address')
    identity_card = fields.Char('Identity Card')
    main_servicer = fields.Char('Servicer', readonly=True)
    is_loyal_customer=fields.Boolean('Loyal Customer', default=False, readonly=True)
    state = fields.Selection([('assigned', 'Assigned'),
                            ('unassigned','Unassigned')],default="unassigned", string="state")

    _sql_constraints = [
        ('phone_uniq', 'UNIQUE (phone)', 'This phone number already exists'),
        ('email_uniq', 'UNIQUE (email)', 'This email already exists'),
    ]

    @api.model
    def default_get(self, fields):
        res = super(CustomerInfo, self).default_get(fields)
        res['email'] = 'abc@gm.uit.vn'
        return res

    def assign_to_me(self):
        self.state = 'assigned'

    def unassigned(self):
        self.state = 'unassigned'
    
    def show_all_transaction(self):
        # a = 1
         return {
            'type': 'ir.actions.act_window',
            'name': _('Transaction'),
            'res_model': 'customer.transaction',
            'view_type': 'tree',
            'view_mode': 'tree',
            'domain': [('patient_id', '=', self.patient_id.id)],
            # 'view_id': self.env.ref("customer_transaction_view_tree").id,
            'target': 'current'
        }

