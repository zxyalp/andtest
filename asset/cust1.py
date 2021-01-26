# -*- coding: utf-8 -*-
"""
Created on 2021/1/15

@author: yang.zhou
"""
update_cust_protocol = '''UPDATE cust_protocol p SET p.protocol_name='{1}', p.change_version='{2}', p.sub_type_code='{3}' WHERE p.product_code='{0}' AND p.tx_acct_no IN  ('1100876065','1100876074','1100876056', '1100876043', '1100876037');'''

cust = '''jywwdxf	我要稳稳的幸福	1265	SP31
tzzhczx	牛基宝<成长型>	1783	SP06
tzzhphx	牛基宝<平衡型>	1763	SP05
tzzhqgx	牛基宝<全股型>	1784	SP22
kcdxzh3	打新计划	1684	SP47
HBYJ	货币赢+	1904	SP08
GJ010	全球赢+10号	42	SP01
GJ018	全球赢+18号	34	SP01
GJ014	全球赢+14号	38	SP01'''

t = cust.split('\n')

for t1 in t:
    print(update_cust_protocol.format(*t1.split()))