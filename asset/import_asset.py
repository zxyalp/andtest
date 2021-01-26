# -*- coding: utf-8 -*-
"""
Created on 2021/1/21

@author: yang.zhou
"""


def insert_high_bash_fund(hbone_no):

    with open('./data/asset_20210121.sql', encoding='utf8') as f, open('asset_{}_out.sql'.format(hbone_no), 'w', encoding='utf8') as w:
        insert_asset_lines = []

        for line in f:
            line = line.replace('8007759556', hbone_no)
            line = line.replace('`id`,', '')
            head, end = line.split('VALUES')
            print(end)
            # print(.split(',')[1:])
            insert_asset_lines.append(line)
        # w.writelines(insert_asset_lines)

        print(insert_asset_lines)


insert_high_bash_fund('8012164906')