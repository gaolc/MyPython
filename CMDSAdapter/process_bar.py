# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 21:37:53 2018

@author: Gao
"""

import time
import logging
import logging.config
import os
import sys
import platform

files='daCMDSAdapter.log'

def getMaxlLineNum(filepath):
    global MAX_LINE_NUM
    if platform.system() == 'Linux':
        # sample ['152234  a.log ']
        r = os.popen('wc -l ' + filepath).readlines()
        # sample 152234
        MAX_LINE_NUM = int(r[0].split(" ")[0])
    elif platform.system()=='Windows':
        with open(filepath) as f:
            text=f.read()
        MAX_LINE_NUM = len(text.splitlines())
    else:
        MAX_LINE_NUM = 445118
    return MAX_LINE_NUM




class ProgressBar():
    """
    显示处理进度的类
    调用该类相关函数即可实现处理进度的显示
    """
    max_arrow = 70
    # 初始化函数，需要知道总共的处理次数
    def __init__(self, max_step):
        self.max_step = max_step
        self.current_step = 1

    # 显示函数，根据当前的处理进度i显示进度
    # 效果为[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>]100.00%
    def updateBar(self, current_step=None):
        if current_step is not None:
            self.current_step = current_step
        num_arrow = int(self.current_step * self.max_arrow / self.max_step)  # 计算显示多少个'>'
        num_line = self.max_arrow - num_arrow  # 计算显示多少个'-'
        percent = self.current_step * 100.0 / self.max_step  # 计算完成进度，格式为xx.xx%
        progress_bar = '[' + '>' * num_arrow + '-' * num_line + ']' + '%.2f' % percent + '%' + '\r'
        progress_bar_r = '[' + '>' * num_arrow + '-' * num_line + ']' + '%.2f' % percent + '%' +'\n'
        if  current_step<self.max_step:
            sys.stdout.write(progress_bar)
        else:
            sys.stdout.write(progress_bar_r)
            self.close()
        sys.stdout.flush()
    def close(self):
        logger.info("Done, result file has been generated at ./result/CMDS_analysis.csv")
        
        
if __name__=="__main__":
