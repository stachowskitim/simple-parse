#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 16:29:15 2018

@author: timothystachowski
"""


import os
import re

cwd = os.getcwd()

valuelist = []



for file in os.listdir(cwd):
	##filename = os.fsdecode(file)
	if file.endswith(".pdb"):			### change for proper file extension
		with open(file) as data:
			stringdata = data.read()
			values = re.findall(r'###',stringdata) ### placeholder for RE
			valuelist.append((file,values))
for value in valuelist:
	print value
	
	
	# For SAXS:
	# "I0": "\w+
	# I1": "\w+
	# diode": "\w+
	# Time": "\w+
	
	#R values from Rosetta refine: \[ final \] R=.+/.+
	
	#For DLS
	# R: .+
	# MW: .+
