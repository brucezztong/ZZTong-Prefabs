#!/usr/bin/python3
import os
import re
import shutil
import string
import sys

#######################################################################
# usage: ./stallion-cbp-rename-part-files.py <Directory>
#######################################################################

extensionsList = [ ".blocks.nim", ".ins", ".jpg", ".mesh", ".tts", ".xml" ]

def renameParts( srcPath ):
    # Loop through the directory looking for XML files. We'll use that
    # file's name to figure out the new name for it and all the other
    # files that go with it.
    for fileName in os.listdir( srcPath ):
        if ( fileName.endswith( ".xml" ) ):
            # First, isolate the file extension from the rest of the filename.
            filesplit = fileName.split( ".", 1 )
            srcFileName = filesplit[0] 

            # Look for files to change...
            poiNameRoot = srcFileName.replace( "part_cp", "part_cbp" )
            poiNameRoot = poiNameRoot.replace( "part_xcp", "part_cbp" )
            poiNameRoot = poiNameRoot.replace( "part_xcostum", "part_cbp" )
            poiNameRoot = poiNameRoot.replace( "part_zztong", "part_cbp" )
            poiNameRoot = poiNameRoot.replace( ".xml", "" )

            for extension in extensionsList:
                os.rename( srcPath + "/" + srcFileName + extension, srcPath + "/" + poiNameRoot + extension )
                print( poiNameRoot + extension )

#######################################################################
#######################################################################

def main():
    if ( len( sys.argv ) != 2 ):
        print( "Usage: stallion-cbp-rename-part-files.py <Directory>" )
        quit()

    dirName = sys.argv[1]
    print( "Changing Directory " + dirName )

    renameParts( dirName )

#######################################################################
#######################################################################

main()
