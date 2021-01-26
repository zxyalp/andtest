# -*- coding: utf-8 -*-
"""
Created on 2021/1/15

@author: yang.zhou
"""


def change_hbone_on(test_hbone_no, pro_hbone_no):
    with open('acc_hbone_no.sql', encoding='utf-8') as a:

        content = a.read()
        cn = content.replace('8012164882', test_hbone_no)
        cn1 = cn.replace('8013210101', pro_hbone_no)
        print(cn1)


pro_no = ['8010085777', '8010070581', '8010048761', '8013133505', '8013130941']
test_no = ['8012164958', '8012164957', '8012164956', '8012164954', '8012164953']

for test, pro in zip(test_no, pro_no):
    change_hbone_on(test, pro)


def insert_cust_protocol():
    with open('inset_cust_protocol.sql', encoding='utf-8') as a:
        content = a.read()
        cn = content.replace('8012164882', test_hbone_no)
        cn1 = cn.replace('8013210101', pro_hbone_no)
        print(cn1)