#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Jack Zhang
Date: 2023/03/26 21:00
"""
import os
import sys

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, '%s/../' % CUR_DIR)
sys.path.insert(0, '%s/../lib/' % CUR_DIR)

def main():
    """
    main
    """
    print("begin to deal!")

if __name__ == "__main__":
    main()