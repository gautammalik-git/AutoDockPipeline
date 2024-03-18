#!/usr/bin/python
import os
import csv
import sys
import copy
from itertools import *
import itertools
import math
import string
import random
import shutil
import getopt
import shlex
import subprocess
from subprocess import call
from subprocess import Popen
import os.path
import glob
import types
import shutil
import re
from time import sleep
import unittest
import time


if len(sys.argv) == 2:
	prot_name = sys.argv[1]
	
	def a():
		a = []
		b = []
		aline = open(prot_name, 'r').readlines()
		for line in aline:
			if line[:4] == "ATOM":
				#print line
				if line[13:16]+" "+line[17:26] not in a:
					b.append(line[:16]+" "+line[17:])
					a.append(line[13:16]+" "+line[17:26])	
		return b
	b = a()
	out = open(prot_name[:-4]+"a.pdb", 'w')
	for line in b:
		out.write(line)
	out.close()
	
		
		
else:
	print("Usage python dock.py <prot_name>")
	sys.exit()
	
	
	
