#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 15:36:52 2019
@author: kayti thorn
"""
import pydicom
import os 
import glob
import os.path

#directory = os.getcwd()

directory = "/Users/kayti/Desktop/Projects/pycomsort_dev/test_data/"
subjids = os.listdir(directory)
if '.DS_Store' in subjids:
  subjids.remove('.DS_Store')

for ids in subjids:  
  path = directory + ids + "/**/*"
  dcmspath = glob.glob(path, recursive=True)
  dcmspath2=dcmspath[100]
  dcmpath = os.path.dirname(dcmspath2)
  dcms = os.listdir(dcmpath)
  if '.DS_Store' in dcms:
      dcms.remove('.DS_Store')
  for dcm in dcms:
      dcmhdr = pydicom.dcmread(dcmpath + '/' + dcm)
      seq = dcmhdr.ProtocolName
      if os.path.exists(directory + '/' + ids + '/' + seq):
          oldfile=os.path.join(dcmpath + '/' + dcm)
          newfile=os.path.join(directory + '/' + ids + '/' + seq + '/' + dcm)
          os.rename(oldfile,newfile)
      else: 
          os.mkdir(directory + '/' + ids + '/' + seq)
          oldfile=os.path.join(dcmpath + '/' + dcm)
          newfile=os.path.join(directory + '/' + ids + '/' + seq + '/' + dcm)
          os.rename(oldfile,newfile)
      for entry in os.scandir(directory + '/' + ids):
        if os.path.isdir(entry.path) and not os.listdir(entry.path) :
          os.rmdir(entry.path)