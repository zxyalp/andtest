# -*- coding: utf-8 -*-
"""
Created on 2021/1/20

@author: yang.zhou
"""
from datetime import datetime
from dateutil.relativedelta import relativedelta

from datetime import datetime, date
from dateutil.relativedelta import relativedelta

now = datetime.now()
print(now)
print(now - relativedelta(months=3))