#!/usr/bin/python3
"""
7 Days to Die TTS decoder
Copyright (C) 2017 Liam Brandt <brandt.liam@gmail.com>
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Modified by ZZTong to analyze a POI instead of display one. That
makes this a derivitive work, so with respect to Liam's wishes this
variation is also protected by the GNU GPL 3.
"""

import struct
import time
import random
import re
import sys
import json
import os

def unpack(bin_file, data_type, length_arg=0):
    #integer or unsigned integer
    if data_type == "i" or data_type == "I":
        return int(struct.unpack(data_type, bin_file.read(4))[0])
    #short or unsigned short
    elif data_type == "h" or data_type == "H":
        return int(struct.unpack(data_type, bin_file.read(2))[0])
    #string
    elif data_type == "s":
        return struct.unpack(str(length_arg) + data_type, bin_file.read(length_arg))[0]
    #char
    elif data_type == "c":
        return struct.unpack(data_type, bin_file.read(1))[0]
    #byte or unsigned byte
    elif data_type == "b" or data_type == "B":
        return int(struct.unpack(data_type, bin_file.read(1))[0])


def main():
    # The name of the POI to analyze should be the command line argument.
    # If the name comes with an extension, strip that off. That can
    # happen if somebody is trying to run the tool across a collection
    # (directory) of POI files. For instance... 7loot.py *.xml
    if ( len( sys.argv ) != 2 ):
        print( "Usage: poi-scout <Directory>" )
        quit()

    dirName = sys.argv[1]
    print( "Directory " + dirName )

    # Setup for Watching Blocks for Special Notes
    inputWatchFileName = "poi-scout-watch.txt"
    inputWatchFile = open( inputWatchFileName, "r" )
    watchDictionary = { }

    for watchLine in inputWatchFile:
        if ( watchLine.startswith( "#" ) == True ):
            continue

        lineList = watchLine.split( ":", 1 )
        watchDictionary.update( { lineList[0].strip(): lineList[1].strip() } )

    # Setup for Output...
    outputBlockSummaryFileName = "poi-scout-blocks.csv"
    outputFileBlocks = open( outputBlockSummaryFileName, "w" )
    outputFileBlocks.write( "POI,Tier,VolumeCount,MinZombies,MaxZombies,Tags,Block,Count,Note\n" )

    #######################################################################################
    # Loop through each POI in the specified directory...
    #######################################################################################

    for fileName in os.listdir( dirName ):
        if ( fileName.endswith( ".xml" ) ):
            print( "File: " + fileName )

            poiName = dirName + "/" + fileName.rsplit( "." )[0]
            size = len( fileName )
            shortName = fileName[:size-4]
    
            blocksFileName = poiName + ".blocks.nim"
            ttsFileName = poiName + ".tts"

            #######################################################################################
            # XML file...
            #######################################################################################

            tier = "0"
            volumeCount = 0         # Total Volume Count for the POI
            zedCountMin = 0         # Total Min Zed Values
            zedCountMax = 0         # Total Max Zed Values

            xmlFile = open(dirName + "/" + fileName, "r")

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
                    valueTags = valueTags.replace( ",", ":" )

            if valueGroupIds != "" and valueGroupDefs != "":
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
                        #print( "range: " + str(zedCountMin) + " - " + str(zedCountMax) )

            xmlFile.close()

            #######################################################################################
            # BLOCKS.NIM File - The names of the blocks.
            #######################################################################################

            blockDesc = {}
            bin_file = open(blocksFileName, "rb")

            versionBlocks = unpack( bin_file, "I" )
            numBlockIDs = unpack( bin_file, "I" )

            for currBlock in range( numBlockIDs ):
                blockID = unpack( bin_file, "I" )
                #blockID = blockID & 2047 -- Too few bits for A20. Not sure when this changed.
                blockID = blockID & 32767

                lenName = unpack( bin_file, "B" )

                myBytes = bytearray()
                for currLetter in range( lenName ):
                    myBytes.append( int.from_bytes( unpack( bin_file, "c" ), "big" ) )

                blockName = myBytes.decode()
                blockDesc[ blockID ] = blockName

                # Debugging
                #print( "blockID: " + str(blockID) + " / blockName: " + blockName )

            # Debugging...
            #print( "blockDesc: ", end="" )
            #print( blockDesc )

            bin_file.close()

            #######################################################################################
            # TTS File - The actual blocks
            #######################################################################################

            bin_file = open(ttsFileName, "rb")

            prefab = {}
            #blockCounts = [0] * 2048 -- Too few bits for A20. Not sure when this changed.
            blockCounts = [0] * 32768

            prefab["header"] = unpack(bin_file, "s", 4)
            prefab["version"] = unpack(bin_file, "I")
            prefab["size_x"] = unpack(bin_file, "H")
            prefab["size_y"] = unpack(bin_file, "H")
            prefab["size_z"] = unpack(bin_file, "H")

            prefab["layers"] = []

            for layer_index in range(prefab["size_z"]):
                prefab["layers"].append([])
                for row_index in range(prefab["size_y"]):
                    prefab["layers"][layer_index].append([])
                    for block_index in range(prefab["size_x"]):
                        prefab["layers"][layer_index][row_index].append(None)
                        value = unpack(bin_file, "I")
                        #get rid of flags, block id can only be less than 2048
                        #block_id = value & 2047 -- Too few bits for A20. Not sure when this changed.
                        block_id = value & 32767
                        flags = value >> 11 # -- No idea what flags are but bits aren't right.

                        prefab["layers"][layer_index][row_index][block_index] = block_id
                        #print( "block_id: " + str( block_id ) )
                        blockCounts[ block_id ] += 1

            bin_file.close()

            #######################################################################################
            # Block Summary...
            # POI,Tier,VolumeCount,MinZombies,MaxZombies,Tags,Block,Count
            #######################################################################################

            for x in range( len( blockCounts ) ):
                if ( blockCounts[x] != 0 ):
                    watchNote = watchDictionary.get( blockDesc[x] )

                    if ( watchNote == None ):
                        outputFileBlocks.write( shortName + "," + tier + "," + str(volumeCount) + "," + str(zedCountMin) + "," \
                        + str(zedCountMax) + "," + valueTags + "," + blockDesc[x] + "," + str( blockCounts[x] ) + ",None\n" )
                    else:
                        outputFileBlocks.write( shortName + "," + tier + "," + str(volumeCount) + "," + str(zedCountMin) + "," \
                        + str(zedCountMax) + "," + valueTags + "," + blockDesc[x] + "," + str( blockCounts[x] ) + \
                        "," + watchNote + "\n" )

    outputFileBlocks.close()

#######################################################################################
# Driver
#######################################################################################

main()
