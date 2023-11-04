#!/usr/bin/python3
import os
import re
import shutil
import string
import sys

#######################################################################
# usage: ./stallion-cbp-rename-part-files.py <Directory>
#######################################################################

def replace_string_in_file( file_path, origString, repString):
    print( "Editing " + file_path )

    # Open the file in read mode and read all lines
    with open( file_path, 'r', encoding='utf-8' ) as file:
        lines = file.readlines()

    # Replace the string in each line
    new_lines = [ line.replace( origString, repString) for line in lines ]

    # Open the file in write mode and write the modified lines back to the file
    with open( file_path, 'w', encoding='utf-8' ) as file:
        file.writelines( new_lines )

#######################################################################
#######################################################################

def renamePartsInXML( srcPath ):
    # Loop through the directory looking for XML files. We'll use that
    # file's name to figure out the new name for it and all the other
    # files that go with it.
    for fileName in os.listdir( srcPath ):
        if ( fileName.endswith( ".xml" ) ):
            replace_string_in_file( srcPath + "/" + fileName, 'part_cp', 'part_cbp')
            replace_string_in_file( srcPath + "/" + fileName, 'part_xcp', 'part_cbp')
            replace_string_in_file( srcPath + "/" + fileName, 'part_xcostum', 'part_cbp')
            replace_string_in_file( srcPath + "/" + fileName, 'part_zztong', 'part_cbp')

#######################################################################
#######################################################################

def main():
    if ( len( sys.argv ) != 2 ):
        print( "Usage: stallion-cbp-rename-part-xml.py <Directory>" )
        quit()

    dirName = sys.argv[1]
    print( "Changing Directory " + dirName )

    renamePartsInXML( dirName )

#######################################################################
#######################################################################

main()
