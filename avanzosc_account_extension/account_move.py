# -*- encoding: utf-8 -*-
##############################################################################
#
#    Avanzosc - Avanced Open Source Consulting
#    Copyright (C) 2011 - 2012 Avanzosc <http://www.avanzosc.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

import time
from datetime import datetime
from operator import itemgetter

import netsvc
from osv import fields, osv
from tools.translate import _
import decimal_precision as dp
import tools

class account_move(osv.osv):
    _inherit = 'account.move'
    
    def apply_changes(self, cr, uid, ids, context=None):
        res = {}
        lines = []
        account_move_line_obj = self.pool.get('account.move.line')
        for account_move in self.browse(cr, uid, ids): 
            for line in account_move.line_id:
                account_move_line_obj.write(cr, uid, [line.id], {'journal_id': account_move.journal_id.id, 'period_id':account_move.period_id.id, 'date':account_move.date})
        return True
    
    def _test_date_in_period(self, cr, uid, ids):
        result = ''
        cur_id = "".join(map(str, ids))
        obj = self.browse(cr, uid, int(cur_id), {})
        period_list = self.pool.get('account.period').find(cr,uid, obj.date)
        if obj.period_id.id not in period_list:
            self.write(cr,uid,[obj.id], {'period_id': period_list[0]})
        return True
    
    _constraints = [
            (_test_date_in_period, '', ['date', 'period_id']),
        ]
account_move()