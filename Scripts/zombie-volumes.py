import os
import sys
import xml.etree.ElementTree as ET

def process_file(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        difficulty_tier = None
        sleeper_volume_groups = []

        # Look for the DifficultyTier and SleeperVolumeGroup properties
        for property in root.findall(".//property"):
            if property.attrib.get("name") == "DifficultyTier":
                difficulty_tier = int(property.attrib.get("value"))
            elif property.attrib.get("name") == "SleeperVolumeGroup":
                value = property.attrib.get("value")
                if value:
                    groups = value.split(',')
                    # Extract zombie types (every third item is the type)
                    types = [groups[i] for i in range(0, len(groups), 3)]
                    sleeper_volume_groups.extend(types)

        # Check the DifficultyTier and print information if tier is 4 or 5
        if difficulty_tier in [4, 5]:
            print()
            print(f"File: {file_path}")
            print(f"Zombie Volume Groups: {', '.join(sleeper_volume_groups)}")

    except ET.ParseError:
        print(f"Failed to parse XML in file: {file_path}")

def process_directory(directory):
    # Loop through all XML files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            file_path = os.path.join(directory, filename)
            process_file(file_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
    else:
        directory = sys.argv[1]
        if os.path.isdir(directory):
            process_directory(directory)
        else:
            print(f"Invalid directory: {directory}")

