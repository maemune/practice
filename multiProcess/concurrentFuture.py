# -*- coding: utf-8 -*-

import sys
sys.dont_write_bytecode = True

import time
import datetime

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

def func_print (n):
    print (n)

def main ():
    # with ProcessPoolExecutor (max_workers = 60) as executor:
    #     for i in range (100000):
    #         executor.submit (func_print (i))
    with ThreadPoolExecutor (max_workers = 1000) as executor:
        for i in range (100000):
            executor.submit (func_print (i))

def setup ():
    start_time = time.time ()
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
