# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2011 Echeverrifm - http://www.echeverrifm.com.ar
#    All Rights Reserved.
#    info echeverrifm (echeverrifm@gmail.com)
############################################################################
#    Coded by: echeverrifm (echeverrifm@gmail.com)
#    Launchpad Project Manager for Publication: Nhomar Hernandez - nhomar@openerp.com.ve
############################################################################
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
    "name" : "MEXICO - DIOT Report",
    "version" : "1.0",
    "depends" : ["base", "base_vat","account", "l10n_mx", "account_accountant", "l10n_mx_account_invoice_tax", "l10n_mx_account_tax_category" ],
    "author" : "Federico Manuel Echeverri Choux",
    "description": """Module DIOT for  Mexico:
    """,
    'author': 'Federico Manuel Echeverri Choux',
    "website" : "http://www.conectel.mx/",
    'init_xml': [],
    'update_xml': [
                    	"partner_view.xml",
#                    	"account_tax_view.xml",
                    	"wizard/wizard_diot_report_view.xml",
                ],
    'installable': True,
    'active': False,
}
