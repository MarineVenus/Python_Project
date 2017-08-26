# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 19:56:53 2017

@author: MasterVenus
"""


import numpy as np
import re,argparse

import sys
import plistlib
from matplotlib import pyplot


def findCommonTracks(fileNames):
    """
    find common tracks in given playlist files,
    and save to common.txt
    """
    trackNameSets=[]
    for fileName in fileNames:
        #create a new set
        trackNames=set()
        plist=plistlib.readPlist(fileName)
        
        #get tracks
        tracks=plist['Tracks']
        #iterate through the tracks
        for trackId,track in tracks.items():
            try:
                #add a name to set
                trackNames.add(track['Name'])
            except:
                #ignore
                pass
        
        #add to a list
        print len(trackNames)
        trackNameSets.append(trackNames)

    print len(trackNameSets)
    
    #get the set of common tracks
    commonTracks=set.intersection(*trackNameSets)
    
    #write to a file
    if len(commonTracks)>0:
        f=open('common.txt','w')
        for val in commonTracks:
            s='%s\n'%val
            f.write(s.encode('UTF-8'))
        f.close()
        print '%d common tracks found.Track names written to common.txt.'%len(commonTracks)
    else:
        print 'No common tracks'
        
Names=['test-data/maya.xml','test-data/rating.xml']

findCommonTracks(Names)
    

f=open('common.txt','r')


data=f.readlines()

for line in data:
    print line


f.close()





















