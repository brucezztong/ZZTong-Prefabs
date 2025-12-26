import os
import re

# #####################################################################
# Places where 7D2D Prefabs can be found...
# 
# C:\Users\zzton\AppData\Roaming\7DaysToDie\Mods\ZZTong-Prefabs
# C:\Program Files (x86)\Steam\steamapps\common\7 Days To Die\Data\Prefabs
# #####################################################################
# For Each Tile
#    Find the District
#    For Each Unique POI Marker Size in ( 100, 60, 42, 25 ) ... or maybe sizes under 25?
#        For Each POI
#            If the POI matches the Size and District
#                Print POI name, tier, and verts
# #####################################################################
# <details>
#     <summary>Tile Name</summary>
#     <ul>
#     ... POIs ...
#     </ul>
# </details>
# #####################################################################

Prefabs = [
    "/mnt/c/Program Files (x86)/Steam/steamapps/common/7 Days To Die/Data/Prefabs",
    "/mnt/c/Users/zzton/AppData/Roaming/7DaysToDie/Mods/ZZTong-Prefabs/Prefabs"
]

GeneratedWorlds = "/mnt/c/Users/zzton/AppData/Roaming/7DaysToDie/GeneratedWorlds"

fieldsPOI = [
    "DifficultyTier",
    "PrefabSize",
    "Tags",
    "TotalVertices"
]

fieldsTile = [
    "POIMarkerSize",
    "TotalVertices"
]

POIs = {}
Tiles = {}
Districts = [ "wilderness" ]
Counts = {}

# #####################################################################
# HTML Header...
# #####################################################################

def writeHeader( file ):
    header = """
<html>
<head><title>RWG Scan</title>
<style> details {
    margin-left: 40px;
}
details > summary {
    margin-left: -40px; cursor: pointer;
}
</style>
</head>
<body>
"""
    file.write( header )

# #####################################################################
# HTML Footer...
# #####################################################################

def writeFooter( file ):
    footer = "\n</body>\n</html>"
    file.write( footer)

# #####################################################################
# Dump all of the world counts...
# #####################################################################

def writeWorlds( file ):
    # For each world...
    for world, counts in Counts.items():
        file.write( f"<details>\n<summary>{world}</summary>\n" )
        file.write( f"<table border=\"1\">\n<tr><th>Tile / POI Name</th><th>Count</th></tr>\n" )

        # For each POI and Tile...
        for name, count in counts.items():
            style = "<style=\"color:black;\""

            if count == 0:
                style = "style=\"color:red;\""

            file.write( f"<tr>\n" )
            file.write( f"<td {style}>{name}</td><td {style}>{count}</td>\n" )
            file.write( f"</tr>\n" )

        file.write( "</table>\n" )
        file.write( "</details>\n" )

# #####################################################################
# Dumps all of the Wilderness POIs...
# #####################################################################

def writeWilderness( file ):
    district = "wilderness"
    file.write( "<details>\n<summary>Wilderness</summary>\n" )
    file.write( f"<table border=\"1\">\n<tr><th>POI Name</th><th>Tier</th><th>Tags</th><th>Vertices</th></tr>\n" )

    # And show each POI that fits into that Marker Size and District...
    for poiName in POIs:
        poiDict = POIs[ poiName ]
        poiTags = poiDict[ "Tags" ]
        poiSize = poiDict[ "PrefabSize" ]
        poiTier = poiDict[ "DifficultyTier" ]
        poiTempVerts = poiDict[ "TotalVertices" ]
        poiVerts = f"{int( poiTempVerts ):,}" 

        if district in poiTags:
            file.write( f"<tr>\n" )
            file.write( f"<td>{poiName}</td>\n" )
            file.write( f"<td>{poiTier}</td>\n" )
            file.write( f"<td>{poiTags}</td>\n" )
            file.write( f"<td>{poiVerts}</td>\n" )
            file.write( f"</tr>\n" )

    file.write( "</table>\n" )
    file.write( "</details>\n" )

# #####################################################################
# Dumps all of the Tiles and their associated POIs...
# #####################################################################

def writeTiles( file ):
    file.write( "<details>\n<summary>Tiles</summary>\n" )

    # First we order the Tiles by District...
    for district in sorted( Districts ):
        if district == "wilderness":
            continue

        file.write( f"<details>\n<summary>{district}</summary>\n" )

        # Then we show each Tile...
        for tile in Tiles:
            if Tiles[ tile ][ "District" ] == district:
                file.write( f"<details>\n<summary>{tile}</summary>\n" )

                # And show each Marker Size on that Tile...
                markers = tileGetUniqueMarkerSizeList( tile )
                for markerSize in markers:
                    displayMarkerSize = markerSize.replace( ", 0, ", "x" )
                    file.write( f"<details>\n<summary>{displayMarkerSize}</summary>\n" )
                    file.write( f"<table border=\"1\">\n<tr><th>POI Name</th><th>Tier</th><th>Tags</th><th>Vertices</th></tr>\n" )

                    # And show each POI that fits into that Marker Size and District...
                    for poiName in POIs:
                        poiDict = POIs[ poiName ]
                        poiTags = poiDict[ "Tags" ]
                        poiSize = poiDict[ "PrefabSize" ]
                        poiTier = poiDict[ "DifficultyTier" ]
                        poiTempVerts = poiDict[ "TotalVertices" ]
                        poiVerts = f"{int( poiTempVerts ):,}" 

                        if district in poiTags and poiSize == markerSize:
                            file.write( f"<tr>\n" )
                            file.write( f"<td>{poiName}</td>\n" )
                            file.write( f"<td>{poiTier}</td>\n" )
                            file.write( f"<td>{poiTags}</td>\n" )
                            file.write( f"<td>{poiVerts}</td>\n" )
                            file.write( f"</tr>\n" )

                    file.write( "</table>\n" )
                    file.write( "</details>\n" )

                file.write( "</details>\n" )

        file.write( "</details>\n" )
    file.write( "</details>\n" )

# #####################################################################
# Dumps all of the POI data and their associated Tiles...
# #####################################################################

def writePOIs( file ):
    file.write( "<details>\n<summary>POIs</summary>\n" )

    for poiName in sorted( POIs ):
        poiDict = POIs[ poiName ]
        poiTags = poiDict[ "Tags" ]
        poiSize = poiDict[ "PrefabSize" ]
        poiTier = poiDict[ "DifficultyTier" ]
        poiTempVerts = poiDict[ "TotalVertices" ]
        poiVerts = f"{int( poiTempVerts ):,}" 

        if poiTags == "Not-Found":
            continue

        file.write( f"<details>\n<summary><b>{poiName}</b> Tier={poiTier}, Size={poiSize}, Tags={poiTags}</summary>\n" )

        # Find all of the Districts for this POI...
        tempDistricts = poiTags.split( ", " )
        for district in tempDistricts:
            if district not in Districts:
                continue

            file.write( f"<details>\n<summary>{district}</summary>\n" )
            file.write( f"<ul>\n" )

            # Find all of the Tiles in that District of the right size...
            for tile in Tiles:
                tileDistrict = Tiles[ tile ][ "District" ]
                tileMarkers = Tiles[ tile ][ "POIMarkerSize" ]

                if district == tileDistrict and tileDistrict in poiTags and poiSize in tileMarkers:
                    file.write( f"<li>\n<summary>{tile}</li>\n" )

            file.write( f"</ul>\n" )
            file.write( "</details>\n" )

        file.write( "</details>\n" )

    file.write( "</details>\n" )

# #####################################################################
# Generate the HTML Results...
# #####################################################################

def writeReport():
    with open( "rwgscan.html", "w" ) as file:
        writeHeader( file )
        writeTiles( file )
        writeWilderness( file )
        writePOIs( file )
        writeWorlds( file )
        writeFooter( file )

# #####################################################################
# These are the properties in a Tile that we want...
# <property name="POIMarkerSize" value="100, 0, 100#42, 0, 42#42, 0, 42#42, 0, 42#42, 0, 42#1, 1, 1#1, 1, 1#1, 1, 1"/>
# <property name="TotalVertices" value="251537"/>
# #####################################################################

def loadTile( filePath, nameTile ):
    print( f"Tile: {nameTile}" )

    thisTile = {}
    for field in fieldsTile:
        thisTile[ field ] = "Not-Found"

    # Check each line of the Tile's XML to find the desired fields...

    with open( filePath ) as file:
        for line in file:
            for field in fieldsTile:
                propertySearchResult = re.search( f"name=\\\"{field}\\\"", line )

                # If we found a matching line, find and save the value...

                if ( propertySearchResult != None ):
                    valueSearchResult = re.search( f"value=\\\".*\\\"", line ).group()
                    value = valueSearchResult[ 7:-1 ]
                    thisTile[ field ] = value

    # Save the complete POI record...
    Tiles[ nameTile ] = thisTile

# #####################################################################
# These are the properties in a POI that we want...
# <property name="DifficultyTier" value="4"/>
# <property name="PrefabSize" value="42, 24, 42"/>
# <property name="Tags" value="commercial"/>
# <property name="TotalVertices" value="752338"/>
# #####################################################################

def loadPOI( filePath, namePOI ):
    print( f"POI: {namePOI}" )

    thisPOI = {}
    for field in fieldsPOI:
        thisPOI[ field ] = "Not-Found"

    # Check each line of the POI's XML to find the desired fields...

    with open( filePath ) as file:
        for line in file:
            for field in fieldsPOI:
                propertySearchResult = re.search( f"name=\\\"{field}\\\"", line )

                # If we found a matching line, find and save the value...

                if ( propertySearchResult != None ):
                    valueSearchResult = re.search( f"value=\\\".*\\\"", line ).group()
                    value = valueSearchResult[ 7:-1 ]
                    thisPOI[ field ] = value

    # Save the complete POI record...
    POIs[ namePOI ] = thisPOI

# #####################################################################
# Given a prefab name, find it, and zero out it's height so that its
# PrefabSize value will match up with POI Marker sizes of Tiles.
# #####################################################################

def poiZeroHeight( poiName ):
    poiDict = POIs[ poiName ]
    poiSize = poiDict[ "PrefabSize" ]

    parts = poiSize.split( ", " )
    if len( parts ) == 3:
        parts[ 1 ] = "0"

    poiDict[ "PrefabSize" ] = ", ".join( parts )

# #####################################################################
# See if a POI's tags include at least one of the known districts...
# #####################################################################

def poiInValidDistrict( poi ):
    tags = poi[ "Tags" ].split( ", " )

    for tag in tags:
        if tag in Districts:
            return True

    return False

# #####################################################################
# Load and transform the POI data...
# #####################################################################

def processPOIs( directory ):
    print( f"processPOIs: {directory}" )

    for subdir, dirs, files in os.walk( directory ):
        for file in files:
            if file.endswith( "xml" ):
                namePOI = file[0:-4]
                loadPOI( os.path.join( subdir, file ), namePOI )

    # Remove the height from the POI Size...
    for poiName in POIs:
        poiZeroHeight( poiName )

# #####################################################################
# #####################################################################

def tileGetUniqueMarkerSizeList( tileName ):
    tileDict = Tiles[ tileName ]
    tileSizes = tileDict[ "POIMarkerSize" ]

    unique = []

    groups = tileSizes.split( "#" )
    for group in groups:
        if group not in unique:
            unique.append( group )

    return unique

# #####################################################################
# Fixing up a Tile's Marker Sizes involves removing dimenstions
# that have a non-zero height as those are parts, not a markers.
# #####################################################################

def tileFixMarkerSizes( tileName ):
    tileDict = Tiles[ tileName ]
    tileSizes = tileDict[ "POIMarkerSize" ]

    filtered = []

    groups = tileSizes.split( "#" )
    for group in groups:
        parts = group.split( ", " )

        if len( parts ) == 3 and parts[ 1 ] == "0":
            filtered.append( group )

    tileDict[ "POIMarkerSize" ] = "#".join( filtered )

# #####################################################################
# Tile districts come from their filename
# This process also creates our unique list of Districts.
# #####################################################################

def tileSetDistrict( tileName ):
    tileDict = Tiles[ tileName ]
    parts = tileName.split( "_" )
    districtName = parts[ 2 ]
    tileDict[ "District" ] = districtName

    if districtName not in Districts:
        Districts.append( districtName )

# #####################################################################
# Load and transform the Tile data...
# #####################################################################

def processTiles( directory ):
    print( f"processTiles: {directory}" )

    for subdir, dirs, files in os.walk( directory ):
        for file in files:
            if file.endswith( "xml" ):
                nameTile = file[0:-4]
                loadTile( os.path.join( subdir, file ), nameTile )

    for tile in Tiles:
        tileFixMarkerSizes( tile )
        tileSetDistrict( tile )

# #####################################################################
# Each directory is a source of data and it can have sub-directories
# for POIs and Tiles...
# #####################################################################

def processDirectory( directory ):
    print( f"processDirectory: {directory}" )

    dirPOIs = directory + "/POIs"
    dirTiles = directory + "/RWGTiles"

    processPOIs( dirPOIs )
    processTiles( dirTiles )

# #####################################################################
# In the GeneratedWorlds Folder there are zero or more game worlds
# that have been built by the user. We're going to mine those worlds
# to count Tiles and POIs...
#
# Data can include Tiles, POIs, and Parts...
# <decoration type="model" name="rwg_tile_ravenswood_intersection_zztong_01" position="-1546,29,-3046" rotation="2" />
# <decoration type="model" name="zztong_red_rocket_01" position="489,44,-1889" rotation="3" />
# <decoration type="model" name="part_zztong_camper_01" position="-1451,38,-2955" rotation="0" />
# ... but we're not interested in Parts, at least not for now.
# #####################################################################

def processWorlds():
    # Loop through each of the generated worlds...
    for subdir, dirs, files in os.walk( GeneratedWorlds ):
        for world in dirs:
            print( f"World: {world}" )

            # Fill in the Counts from the list of known Tiles and POIs...
            Counts[ world ] = {}

            for tile in sorted( Tiles ):
                Counts[ world ][ tile ] = 0

            for poiName, poiData in POIs.items():
                if poiInValidDistrict( poiData ) == True:
                    Counts[ world ][ poiName ] = 0

            filePrefabs = os.path.join( subdir, world ) + "/prefabs.xml"

            # Loop through the prefabs.xml file for the current world...
            with open( filePrefabs ) as file:
                for line in file:
                    nameSearchResult = re.search( r'name=\"(.+?)\"', line )

                    if nameSearchResult != None:
                        name = nameSearchResult.group( 1 )

                        if name in Counts[ world ]:
                            Counts[ world ][ name ] = Counts[ world ][ name ] + 1

# #####################################################################
# Driver...
# #####################################################################

def driver():
    # RWG Data...
    for currDir in Prefabs:
        processDirectory( currDir )

    # RWG Results ... (Generated Worlds)
    processWorlds()

    # Write out all of the results...
    writeReport()


if __name__ == "__main__":
    driver()

