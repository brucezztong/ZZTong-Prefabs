#!/usr/bin/python3
import os
import re
import shutil
import string
import sys

#######################################################################
# Loop through all files for the given source path and copy the files
# to a destination path, converting from the ZZTong naming convention
# to the CompoPack naming convention...
#
# zztong_apartment_01.xml ==> xcp_Apartment_01(by_ZZTong).xml
#######################################################################

# Files of these types have to be renamed to meet CP conventions...
# Decorations and POIs get renamed. Parts and Tiles do not.
renameList = [ "Decorations", "POIs" ]
extensionsList = [ ".blocks.nim", ".ins", ".jpg", ".mesh", ".tts", ".xml" ]

def exportFiles( srcPath, dstPath, poiType ):
    # Loop through each file in the source directory...
    for fileName in os.listdir( srcPath ):
        if ( fileName.endswith( ".xml" ) ):
            # First, isolate the file extension from the rest of the filename.
            filesplit = fileName.split( ".", 1 )
            srcFileName = filesplit[0]

            # Assume the file doesn't get renamed...
            dstFilename = srcFileName

            # If the file must be renamed, then devise the new name...
            if ( poiType in renameList ): 
                # Remove the modlet filename's prefix and suffix information
                poiNameRoot = srcFileName.replace( "zztong_", "" )
                poiNameRoot = poiNameRoot.replace( ".xml", "" )
                # Stallion likes mixed case names, so upper any letter that follows an underscore
                poiNameRoot = string.capwords( poiNameRoot, sep='_' )
                # Append the CP prefix and suffix
                poiNameRoot = "xcp_" + poiNameRoot + "_ZZTong"
                # Fix unique naming issues...
                poiNameRoot = poiNameRoot.replace( "_Destroyed_", "_Dest_" )
                poiNameRoot = poiNameRoot.replace( "_Ems_", "_EMS_" )
                poiNameRoot = poiNameRoot.replace( "_Kzmb_", "_KZMB_" )
                poiNameRoot = poiNameRoot.replace( "_Kztv_", "_KZTV_" )
                poiNameRoot = poiNameRoot.replace( "_Tfp_", "_TFP_" )
                poiNameRoot = poiNameRoot.replace( "_Xs_", "_XS_" )

            else:
                poiNameRoot = srcFileName.replace( ".xml", "" )

            for extension in extensionsList:
                shutil.copy2( srcPath + "/" + srcFileName + extension, dstPath + "/" + poiNameRoot + extension )
                print( poiNameRoot + extension )

#######################################################################
# Driver
#######################################################################

poiPath = "../Prefabs/"
configPath = "../Config/"
stampPath = "../Stamps/"
copyPathTop = "../CP-Export/"
copyPathPrefabs = copyPathTop + "Prefabs/"
subDirsTop = [ "Config", "Prefabs", "Stamps" ]
subDirsPrefab = [ "Decorations", "Parts", "POIs", "RWGTiles" ]

# Prepare destination paths...
if ( os.path.exists( copyPathTop ) == True ):
    print( "The script will not overwrite the 'CP-Export' directory." )
    print( "Remove that directory if you want the script to run." )
    exit( 10 )
else:
    # Create the destination directories...
    os.makedirs( copyPathTop )

    for subDir in subDirsTop:
        os.makedirs( copyPathTop + subDir )

    for subDir in subDirsPrefab:
        os.makedirs( copyPathPrefabs + subDir )

# Drive the POI files export conversion...
for subDir in subDirsPrefab:
    exportFiles( poiPath + subDir, copyPathPrefabs + subDir, subDir )

# Config files export...
for fileName in os.listdir( configPath ):
    shutil.copy2( configPath + "/" + fileName, copyPathTop + "Config/" )
    print( fileName )

# Stamp files export...
for fileName in os.listdir( stampPath ):
    shutil.copy2( stampPath + "/" + fileName, copyPathTop + "Stamps/" )
    print( fileName )
