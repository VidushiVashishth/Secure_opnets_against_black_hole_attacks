#!/usr/bin/env python

import os
import sys
import time

os.system('cd C:/Users\Vidushi\Downloads\one_1.5.0-RC1')

indexer = 1
looper = 8


while(looper > 0):

    looper -= 1

    
    os.system('./one.sh -b ' + str(indexer) + ':' + str(indexer))
    indexer += 1
#    time.sleep(67)

    with open("C:/Users\Vidushi\Downloads\one_1.5.0-RC1/reports\default_scenario_MessageStatsReport.txt") as data:
        for i, line  in enumerate(data):
            if i == 9:

                if looper == 7:
                    newfile = open("C:/Users\Vidushi\Downloads\one_1.5.0-RC1/anshumanHelpers\data.csv", "w")

                elif looper < 7:
                    newfile = open("C:/Users\Vidushi\Downloads\one_1.5.0-RC1/anshumanHelpers\data.csv", "a") 
                    
                newfile.writelines(line + "\n")


                
