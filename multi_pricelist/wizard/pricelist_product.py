# -*- coding: utf-8 -*-
################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Bhagyadev KP (odoo@cybrosys.com)
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
################################################################################
from odoo import fields, models


class PricelistProduct(models.TransientModel):
    """This class will create a new transient model for the price list wizard"""
    _name = 'pricelist.product'
    _rec_name = 'order_line_id'
    _description = 'Price list product'

    order_line_id = fields.Many2one('sale.order.line',
                                    string="Order Line",
                                    help="Order line of the selected order")
    line_ids = fields.One2many('pricelist.line', 'wizard_id',
                               string="Price lists", help="Pricelist lines")

