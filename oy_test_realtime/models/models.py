# -*- coding: utf-8 -*-

import uuid
from odoo import models, fields, api,  _


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    def action_test_realtime(self):
        self.env.user._bus_send('realtime_oy_channel', {'Live Data': 'Data Update', 'Test': 'Test'})