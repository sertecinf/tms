# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012 HESATEC (<http://www.hesatecnica.com>).
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
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Freight Management",
    "version": "1.0",
    "category": "Vertical",
    'complexity': "normal",
    "author": "HESATEC",
    "website": "http://www.hesatecnica.com",
    "depends": ["hr", "account_voucher", "purchase", "sale", "fleet"],
    "summary": "Management System for Carriers, Trucking and other companies",
    "data": [
        'security/ir.model.access.csv',
        'views/tms_view.xml',
        # 'views/account_journal_view.xml',
        # 'views/fleet_vehicle_odometer_view.xml',
        # 'views/fleet_vehicle_view.xml',
        'views/hr_employee_view.xml',
        # 'views/product_category_view.xml',
        # 'views/product_product_view.xml',
        # 'views/tms_advance_view.xml',
        # 'views/tms_config_settings_view.xml',
        # 'views/tms_expense_line_view.xml',
        # 'views/tms_expense_view.xml',
        # 'views/tms_factor_view.xml',
        'views/tms_place_view.xml',
        # 'views/tms_route_view.xml',
        # 'views/tms_travel_view.xml',
        # 'views/tms_unit_kit_view.xml',
        # 'views/tms_waybill_view.xml',
    ],
    "demo": [
        'demo/tms_place.xml'
    ],
    "application": True,
    "installable": True
}