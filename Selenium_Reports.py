'''
Created on Mar 27, 2019

@author: vkhoday
'''
import allure
import os
from os.path import _get_bothseps, _getfullpathname


def gpath (path):
    if path:
        path = os.fspath(path)
        fpath = _getfullpathname(path)
        return fpath
    elif isinstance(path,bytes):
        fpath = os.getcwdb()
    else:
        fpath = os.getcwd()
        
    return fpath

rr =gpath(None)
print(rr)
