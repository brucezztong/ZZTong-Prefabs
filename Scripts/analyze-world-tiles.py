#!/usr/bin/python3
import os
import xml.etree.ElementTree as ET
from collections import defaultdict

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

# List of allowed names to check
allowed_names = [
"rwg_tile_commercial_cap",
"rwg_tile_commercial_cap_zztong_01",
"rwg_tile_commercial_corner",
"rwg_tile_commercial_intersection",
"rwg_tile_commercial_intersection_zztong_01",
"rwg_tile_commercial_straight",
"rwg_tile_commercial_t",
"rwg_tile_commercial_t_zztong_01",
"rwg_tile_countryresidential_cap",
"rwg_tile_countryresidential_cap_zztong_01",
"rwg_tile_countryresidential_corner",
"rwg_tile_countryresidential_corner_zztong_01",
"rwg_tile_countryresidential_corner_zztong_02",
"rwg_tile_countryresidential_intersection",
"rwg_tile_countryresidential_straight",
"rwg_tile_countryresidential_straight_03",
"rwg_tile_countryresidential_straight_zztong_01",
"rwg_tile_countryresidential_t",
"rwg_tile_countryresidential_t_zztong_01",
"rwg_tile_countrytown_cap",
"rwg_tile_countrytown_corner",
"rwg_tile_countrytown_intersection",
"rwg_tile_countrytown_straight",
"rwg_tile_countrytown_t",
"rwg_tile_countrytown_t_zztong_01",
"rwg_tile_downtown_cap",
"rwg_tile_downtown_corner",
"rwg_tile_downtown_intersection",
"rwg_tile_downtown_intersection_02",
"rwg_tile_downtown_intersection_zztong_01",
"rwg_tile_downtown_intersection_zztong_02",
"rwg_tile_downtown_intersection_zztong_03",
"rwg_tile_downtown_intersection_zztong_04",
"rwg_tile_downtown_straight",
"rwg_tile_downtown_t",
"rwg_tile_gateway_intersection",
"rwg_tile_gateway_intersection2",
"rwg_tile_gateway_intersection_zztong_01",
"rwg_tile_gateway_intersection_zztong_02",
"rwg_tile_gateway_intersection_zztong_03",
"rwg_tile_gateway_straight",
"rwg_tile_gateway_straight2",
"rwg_tile_gateway_straight3",
"rwg_tile_gateway_straight3a",
"rwg_tile_gateway_straight3b",
"rwg_tile_gateway_straight4",
"rwg_tile_gateway_straight_zztong_01",
"rwg_tile_gateway_straight_zztong_02",
"rwg_tile_gateway_straight_zztong_03",
"rwg_tile_gateway_straight_zztong_04",
"rwg_tile_gateway_straight_zztong_05",
"rwg_tile_gateway_straight_zztong_06",
"rwg_tile_gateway_straight_zztong_07",
"rwg_tile_gateway_straight_zztong_08",
"rwg_tile_gateway_t",
"rwg_tile_gateway_t_zztong_01",
"rwg_tile_gateway_t_zztong_02",
"rwg_tile_industrial_cap",
"rwg_tile_industrial_corner",
"rwg_tile_industrial_intersection",
"rwg_tile_industrial_straight",
"rwg_tile_industrial_t",
"rwg_tile_oldwest_cap",
"rwg_tile_oldwest_corner",
"rwg_tile_oldwest_intersection",
"rwg_tile_oldwest_straight",
"rwg_tile_oldwest_t",
"rwg_tile_residential_cap",
"rwg_tile_residential_cap_zztong_01",
"rwg_tile_residential_corner",
"rwg_tile_residential_corner_zztong_01",
"rwg_tile_residential_intersection",
"rwg_tile_residential_intersection_zztong_01",
"rwg_tile_residential_straight",
"rwg_tile_residential_straight_zztong_01",
"rwg_tile_residential_straight_zztong_02",
"rwg_tile_residential_t",
"rwg_tile_residential_t_zztong_01",
"rwg_tile_residential_t_zztong_02",
"rwg_tile_rural_cap",
"rwg_tile_rural_cap_zztong_01",
"rwg_tile_rural_cap_zztong_02",
"rwg_tile_rural_cap_zztong_03",
"rwg_tile_rural_corner",
"rwg_tile_rural_corner_02",
"rwg_tile_rural_corner_03",
"rwg_tile_rural_corner_zztong_01",
"rwg_tile_rural_corner_zztong_02",
"rwg_tile_rural_corner_zztong_03",
"rwg_tile_rural_corner_zztong_04",
"rwg_tile_rural_corner_zztong_05",
"rwg_tile_rural_corner_zztong_06",
"rwg_tile_rural_intersection",
"rwg_tile_rural_intersection_zztong_01",
"rwg_tile_rural_straight",
"rwg_tile_rural_straight_zztong_01",
"rwg_tile_rural_t",
"rwg_tile_rural_t_02",
"rwg_tile_rural_t_03",
"rwg_tile_rural_t_04",
"rwg_tile_rural_t_zztong_01",
"rwg_tile_rural_t_zztong_02",
"rwg_tile_rural_t_zztong_03",
"rwg_tile_rural_t_zztong_04",
"rwg_tile_rural_t_zztong_05",
]

# Count the unique prefab names
count_unique_prefabs(base_path, allowed_names)

