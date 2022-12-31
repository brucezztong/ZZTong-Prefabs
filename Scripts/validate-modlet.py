#!/usr/bin/python3
import os
import sys

# Loop through all the XML files in the directory and attempt to find the
# other POI files with the same name (case sensitive).

def checkPath( path ):
    print( "Evaluating " + path + " ..." )

    for files in os.listdir( path ):
        if files.endswith( ".xml" ):
            basefn = files.rsplit( ".", 1 )[0]

            fn = basefn + ".blocks.nim"
            if os.path.isfile( path + "/" + fn ) == False:
                print( "Did not find " + fn )

            fn = basefn + ".ins"
            if os.path.isfile( path + "/" + fn ) == False:
                print( "Did not find " + fn )

            fn = basefn + ".jpg"
            if os.path.isfile( path + "/" + fn ) == False:
                print( "Did not find " + fn )

            fn = basefn + ".mesh"
            if os.path.isfile( path + "/" + fn ) == False:
                print( "Did not find " + fn )

            fn = basefn + ".tts"
            if os.path.isfile( path + "/" + fn ) == False:
                print( "Did not find " + fn )

        else:
            continue

# Driver

checkPath( "../Prefabs/Decorations" )
checkPath( "../Prefabs/Parts" )
checkPath( "../Prefabs/POIs" )
checkPath( "../Prefabs/RWGTiles" )
