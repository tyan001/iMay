# -*- coding: utf-8 -*-
"""
Created on Fri May 10 12:29:17 2019

@author: Thony
"""
import shutil
def zipFiles(outputFileNames, dirNames):
    
    outputs = outputFileNames
    inputs = dirNames
    for i in range(len(inputs)):
        shutil.make_archive(outputs[i], 'zip', inputs[i])
#    for i in range(len(args1)):
#        print(args1[i])
#    for j in range(len(args2)):
#        print(args2[j])

    


    