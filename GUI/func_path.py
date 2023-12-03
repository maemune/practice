# -*- coding: utf-8 -*-
import sys
sys.dont_write_bytecode = True

from tkinter import filedialog
import os

def main (flag): # Option True:FileSelect False:DirSelect
    fType = [('', '*')] #file_type
    curDir = os.path.dirname (__file__) #current_dir
    curDir_FullPath = os.path.abspath (curDir) #current_dir_FullPath
    path_name = filedialog.askopenfilenames (filetypes = fType, initialdir = curDir_FullPath) \
        if flag else filedialog.askdirectory (initialdir = curDir_FullPath) #open_select_dir_FullPath
    return path_name [0] if len (path_name) <= 1 else path_name

if __name__ == '__main__':
    print (main (True))
