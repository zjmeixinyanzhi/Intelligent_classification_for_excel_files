#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Jack Zhang
Date: 2023/03/26 21:00
"""
import os
import sys
import logging
import pandas as pd

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, '%s/../' % CUR_DIR)
sys.path.insert(0, '%s/../lib/' % CUR_DIR)

import log
log.init_log("%s/../log/process" % CUR_DIR, logger_name='process')
logger = logging.getLogger("process")

def main():
    """
    main
    """
    print("begin to deal!")

    demo_file = "%s/../data/need_process_dir/demo.xlsx" % CUR_DIR
    logger.info(demo_file)

    # pd.set_option('display.notebook_repr_html', False)
    content = pd.read_excel(io=demo_file, sheet_name=0)
    print(content)




if __name__ == "__main__":
    main()