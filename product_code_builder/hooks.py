# -*- coding: utf-8 -*-
# © 2016 Akretion (http://www.akretion.com)
# Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


def pre_init_hook(cr):
    cr.execute("""ALTER TABLE product_product
        ADD COLUMN manual_default_code VARCHAR""")
    cr.execute("""UPDATE product_product
        SET manual_default_code = default_code""")
