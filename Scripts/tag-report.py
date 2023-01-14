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
        print( "Usage: python3 tag-report.py <Directory>" )
        quit()

    dirName = sys.argv[1]
    print( "Directory " + dirName )

    outputFileName = "tag-report.txt"

    outputFile = open( outputFileName, "w" )

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

            poiName = dirName + "/" + fileName.rsplit( "." )[0]
            size = len( fileName )
            shortName = fileName[:size-4]
    
            xmlFile = open(dirName + "/" + fileName, "r")

            #######################################################################################
            # Gather data...
            #######################################################################################

            valueTags = ""

            for line in xmlFile:
                if "name=\"Tags\"" in line:
                    valueTags = re.findall( "value=\"(.*?)\"", line )[0]

            #######################################################################################
            # Process the results...
            #######################################################################################

            #######################################################################################
            # Save the results...
            #######################################################################################

            outputFile.write( shortName )
            outputFile.write( " :  " + valueTags )
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
