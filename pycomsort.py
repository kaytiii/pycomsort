#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 15:36:52 2019

@author: kayti
"""

import pydicom
import os 

path = os.getcwd()
#path='/Users/kayti/Desktop/Projects/Tests/pycomsort_test'

subjids = os.listdir(path)
subjids.remove('.DS_Store')

for ids in subjids:
    dcms = os.listdir(path + '/' + ids + '/dicom')
    if '.DS_Store' in dcms:
        dcms.remove('.DS_Store')
    for dcm in dcms:
        dcmhdr = pydicom.dcmread(path + '/' + ids + '/dicom/' + dcm)
        seq = dcmhdr.ProtocolName
        if os.path.exists(path + '/' + ids + '/dicom/' + seq):
            oldfile=os.path.join(path + '/' + ids + '/dicom/' + dcm)
            newfile=os.path.join(path + '/' + ids + '/dicom/' + seq + '/' + dcm)
            os.rename(oldfile,newfile)
        else: 
            os.mkdir(path + '/' + ids + '/dicom/' + seq)
            oldfile=os.path.join(path + '/' + ids + '/dicom/' + dcm)
            newfile=os.path.join(path + '/' + ids + '/dicom/' + seq + '/' + dcm)
            os.rename(oldfile,newfile)
