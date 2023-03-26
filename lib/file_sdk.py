#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Jack Zhang
Date: 2021/07/07 13:00
"""

import os

class FileOpsSdk(object):
    """ File Ops Sdk """

    def read_file(self, file):
        """
        read file to lines
        """
        content_list = []
        try:
            with open(file, 'r') as f:
                for line in f.readlines():
                    line = line.split("\n")[0]
                    content_list.append(line)
        except Exception as e:
            print(e)

        return content_list

    def write_file(self, file_name, content_list):
        """
        write file to content
        """
        try:
            with open(file_name, "w+") as f:
                for line in content_list:
                    f.write("%s\n" % line.encode(encoding='UTF-8'))
            return True
        except Exception as e:
            print(e)
        return False