#!/usr/bin/python3

#import struct
#import time
#import random
#import json

import os
import re
import sys

def main():
    # The directory name to be searched should be in the command line arguments.
    if ( len( sys.argv ) != 2 ):
        print( "Usage: python3 parts-check.py <Directory>" )
        quit()

    dirName = sys.argv[1]
    print( "Directory " + dirName )

    outputFileName = "parts-check-results.csv"

    outputFile = open( outputFileName, "w" )
    outputFile.write( "POI,Part\n" )

    #######################################################################################
    #######################################################################################

    #######################################################################################
    # Loop through each POI or Tile in the specified directory...
    #######################################################################################

    for fileName in os.listdir( dirName ):
        if ( fileName.endswith( ".xml" ) ):
            print( "File: " + fileName )

            #######################################################################################
            # Prepare to read/parse XML file...
            #######################################################################################

            poiName = dirName + "/" + fileName.rsplit( "." )[0]
            size = len( fileName )
            shortName = fileName[:size-4]
    
            xmlFile = open(dirName + "/" + fileName, "r")

            #######################################################################################
            # Gather data...
            #######################################################################################

            for line in xmlFile:
                if "name=\"POIMarkerPartToSpawn\"" in line:
                    parts = re.findall( "value=\"(.*?)\"", line )[0]

                    #######################################################################################
                    # Process the results...
                    #######################################################################################

                    partsList = parts.split( ",", -1 )
                    numParts = len(partsList)

                    for p in range( numParts ):
                        if partsList[p] != "":
                            outputFile.write( shortName )
                            outputFile.write( "," + partsList[p] )
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
