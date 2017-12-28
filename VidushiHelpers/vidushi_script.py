#!/usr/bin/env python

import subprocess
import os
import time

os.chdir(r'''C:\Users\Vidushi\Downloads\one_1.5.0-RC1''')

l = 8
indexer = 1

while (l>0):

	l = l-1
	subprocess.Popen(['one.bat', '-b', str(indexer)+':'+str(indexer)])
	indexer += 1

	time.sleep(120)

	with open(r'''C:\Users\Vidushi\Downloads\one_1.5.0-RC1\reports\default_scenario_MessageStatsReport.txt''') as data:
		for i, line in enumerate(data):
			if i == 9:

				if l == 7:
					newfile = open(r'''C:\Users\Vidushi\Downloads\one_1.5.0-RC1\anshumanHelpers\data.csv''', "w")

				elif l<7:
					newfile = open(r'''C:\Users\Vidushi\Downloads\one_1.5.0-RC1\anshumanHelpers\data.csv''', "a")

				newfile.writelines(line + "\n")


