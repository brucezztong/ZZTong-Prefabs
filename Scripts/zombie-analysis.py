#!/usr/bin/python3

#import struct
#import time
#import random
#import json

import os
import re
import sys

def main():
    # The name of the POI to analyze should be the command line argument.
    # If the name comes with an extension, strip that off. That can
    # happen if somebody is trying to run the tool across a collection
    # (directory) of POI files. For instance... 7loot.py *.xml
    if ( len( sys.argv ) != 2 ):
        print( "Usage: python3 zombie-analysis.py <Directory>" )
        quit()

    dirName = sys.argv[1]
    print( "Directory " + dirName )

    outputFileName = "zombie-analysis.csv"

    outputFile = open( outputFileName, "w" )
    outputFile.write( "POI,Tier,NumVolumes,MinZeds,MaxZeds\n" )

    #######################################################################################
    #######################################################################################

    #######################################################################################
    # Loop through each POI in the specified directory...
    #######################################################################################

    for fileName in os.listdir( dirName ):
        if ( fileName.endswith( ".xml" ) ):
            print( "File: " + fileName )

            #######################################################################################
            # Prepare to read/parse XML file...
            #######################################################################################

            tier = "0"
            volumeCount = 0         # Total Volume Count for the POI
            zedCountMin = 0         # Total Min Zed Values
            zedCountMax = 0         # Total Max Zed Values

            poiName = dirName + "/" + fileName.rsplit( "." )[0]
            size = len( fileName )
            shortName = fileName[:size-4]
    
            xmlFile = open(dirName + "/" + fileName, "r")

            #######################################################################################
            # Gather data...
            #######################################################################################

            valueGroupIds = ""
            valueGroupDefs = ""
            valueTags = ""

            for line in xmlFile:
                if "name=\"DifficultyTier\"" in line:
                    tier = re.findall( "value=\"(.*?)\"", line )[0]

                if "name=\"SleeperVolumeGroupId\"" in line:
                    valueGroupIds = re.findall( "value=\"(.*?)\"", line )[0]

                if "name=\"SleeperVolumeGroup\"" in line:
                    valueGroupDefs = re.findall( "value=\"(.*?)\"", line )[0]

                if "name=\"Tags\"" in line:
                    valueTags = re.findall( "value=\"(.*?)\"", line )[0]

            # if there are no Tags, then the POI will be ignored by RWG. It is a sign the POI isn't finished.
            # A "navonly" POI is also not used by RWG.
            # The same is true if there are no zombie volumes.
            if valueGroupIds == "" or valueGroupDefs == "" or valueTags == "" or valueTags == "navonly":
                print( "Skipping because missing zombie volume XML tags or POI tags." )
                continue

            #######################################################################################
            # Process the results...
            #######################################################################################

            # How many volumes?
            valueList = valueGroupIds.split( ",", -1 )
            workingVolumeCount = len( valueList )

            # Volume specific values...
            valueList = valueGroupDefs.split( ",", -1 )

            if workingVolumeCount > 0:
                for i in range( workingVolumeCount ):
                    volumeZeds = valueList[i*3]
                    zedMin = int(valueList[i*3+1])
                    zedMax = int(valueList[i*3+2])

                    # Skip volumes with no zombies.
                    if zedMin < 1 and zedMax < 1:
                        continue

                    volumeCount = volumeCount + 1
                    zedCountMin += int(valueList[i*3+1])
                    zedCountMax += int(valueList[i*3+2])
                    print( "range: " + str(zedCountMin) + " - " + str(zedCountMax) )

            #######################################################################################
            # Save the results...
            #######################################################################################

            outputFile.write( shortName )
            outputFile.write( "," + tier )
            outputFile.write( "," + str(volumeCount) )
            outputFile.write( "," + str(zedCountMin) )
            outputFile.write( "," + str(zedCountMax) )
            outputFile.write( "\n")

            #######################################################################################
            # Done with this XML file...
            #######################################################################################

            xmlFile.close()

            #######################################################################################
            #######################################################################################

    outputFile.close()

#######################################################################################
# Driver
#######################################################################################

main()
