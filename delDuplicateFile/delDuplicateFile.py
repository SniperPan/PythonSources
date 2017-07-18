#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os

file = open('filesHere.txt', 'w')

class delDuplicateFile():
	def __init__(self, dir):
		filesHere = []
		filesDuplicated = []
		for root, dirs, files in os.walk(dir):
			for name in files:
				if name[:-4] in ''.join(map(str, filesHere)):
					if not name.endswith('.azw3'):
						filesDuplicated.append(os.path.join(root, name))
						os.remove(os.path.join(root, name))
				else: 
					filesHere.append(name)
					#make txt for all files
					file.write(os.path.join(root, name) + '\n')
		
		#print(filesHere)
		if len(filesDuplicated) > 0:
			print("Duplicated Files Which deleted are list below:")
			print(filesDuplicated)
		else:
			print("No duplicated files, Quit now!")
				
		
if(__name__ == "__main__"):
	delDuplicateFile(sys.argv[1])
	