import os
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict

def count_tiers_in_xml_files(root_path):
    tier_count = defaultdict(int)

    # Walk through all directories and files starting from root_path
    for dirpath, _, filenames in os.walk(root_path):
        for filename in filenames:
            if filename.endswith(".xml"):
                file_path = os.path.join(dirpath, filename)
                print( f"File: {file_path}" )
                try:
                    # Parse the XML file
                    tree = ET.parse(file_path)
                    root = tree.getroot()
                    
                    # Look for the property element with name="Tier"
                    for elem in root.findall(".//property"):
                        if elem.attrib.get("name") == "DifficultyTier":
                            tier_value = elem.attrib.get("value", "None")
                            tier_count[tier_value] += 1
                except ET.ParseError:
                    print(f"Error parsing {file_path}, skipping.")
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

    return tier_count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_tiers.py <directory_path>")
        sys.exit(1)

    root_directory = sys.argv[1]

    if not os.path.exists(root_directory):
        print(f"Path {root_directory} does not exist.")
        sys.exit(1)

    # Count the tiers in XML files
    result = count_tiers_in_xml_files(root_directory)

    # Print the results
    print("Tier counts in XML files:")
    for tier, count in sorted(result.items(), key=lambda item: item[0]):
        print(f"Tier: {tier}, Count: {count}")
