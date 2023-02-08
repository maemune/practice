# -*- coding: utf-8 -*-

import sys
sys.dont_write_bytecode = True

import os
import time
import datetime
import logging.config

def main ():
    # ログ設定ファイルからログ設定を読み込み
    logging.config.fileConfig ('logging.conf')

    logger = logging.getLogger ()

    logger.log (20, 'info')
    logger.log (30, 'warning')
    logger.log (100, 'test')

    logger.info ('info')
    logger.warning ('warning')

def setup ():
    start_time = time.time ()
    if not os.path.isdir ('log/'):
        os.makedirs ('log/')

    main ()

    end_time = time.time ()
    print ()#Line Feed
    print ('>>> {} sec'.format (round (end_time - start_time, 1)))

def time_stamp ():
    t_delta = datetime.timedelta (hours = 9)
    JST = datetime.timezone (t_delta, 'JST')
    now = datetime.datetime.now (JST)
    return now.strftime ('%Y_%m_%d_%H_%M_%S')

if __name__ == '__main__':
    setup ()
    sys.exit ()