#!/usr/bin/python3
import os
import xml.etree.ElementTree as ET
from collections import defaultdict

def build_allowed_names():
    tile_dirs = [
        "/mnt/c/Program Files (x86)/Steam/steamapps/common/7 Days To Die/Data/Prefabs/RWGTiles",
        "/mnt/c/Users/zzton/AppData/Roaming/7DaysToDie/Mods/ZZTong-Prefabs/Prefabs/RWGTiles",
    ]
    names = set()
    for d in tile_dirs:
        if os.path.isdir(d):
            for f in os.listdir(d):
                if f.lower().endswith('.xml'):
                    names.add(os.path.splitext(f)[0])
    return sorted(names)

def process_directory(xml_file, allowed_names):
    # Initialize counts for each name in the allowed list to zero
    unique_counts = defaultdict(int, {name: 0 for name in allowed_names})
    
    try:
        # Parse the XML file
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        # Iterate over each decoration element
        for decoration in root.findall('.//decoration[@type="model"]'):
            name = decoration.get('name')
            
            # Update count if the name is in the allowed names list
            if name in allowed_names:
                unique_counts[name] += 1
    
    except ET.ParseError:
        print(f"Error parsing XML in {xml_file}")
    
    return unique_counts

def count_unique_prefabs(base_path, allowed_names):
    # Path where the directories are located
    path = os.path.expanduser(base_path)
    
    # Running total counts across all directories
    total_counts = defaultdict(int, {name: 0 for name in allowed_names})
    
    # Loop through each directory in the specified path
    for directory in os.listdir(path):
        full_path = os.path.join(path, directory)
        
        # Ensure it is a directory
        if os.path.isdir(full_path):
            xml_file = os.path.join(full_path, 'prefabs.xml')
            
            # Check if prefabs.xml exists in this directory
            if os.path.exists(xml_file):
                # Process each directory individually
                unique_counts = process_directory(xml_file, allowed_names)
                
                # Update running total counts
                for name in allowed_names:
                    total_counts[name] += unique_counts[name]
                
                # Print the results for the current directory
                print(f"Directory: {directory}")
                for name in sorted(allowed_names):
                    print(f"{name}: {unique_counts[name]}")
                print("------")  # Separator for clarity
    
    # Print total counts after processing all directories
    print("Total Counts Across All Directories:")
    for name in sorted(allowed_names):
        print(f"{name}: {total_counts[name]}")

# Define the path to the directory containing the worlds
base_path = '~/7d2d/GeneratedWorlds'

# Build the allowed names list dynamically from the tile prefab directories
allowed_names = build_allowed_names()
print( "ZZ:", allowed_names )

# Count the unique prefab names
count_unique_prefabs(base_path, allowed_names)

