import csv
import time
from googletrans import Translator

# Define input and output file paths
INPUT_FILE = "../Config/Localization.txt"
OUTPUT_FILE = "Localization-Trans.txt"

# Define language columns (ISO 639-1 codes for Google Translate)
LANGUAGE_MAP = {
    "german": "de",
    "spanish": "es",
    "french": "fr",
    "italian": "it",
    "japanese": "ja",
    "koreana": "ko",
    "polish": "pl",
    "brazilian": "pt",
    "russian": "ru",
    "turkish": "tr",
    "schinese": "zh-cn",
    "tchinese": "zh-tw"
}

# Initialize Google Translator
translator = Translator()

# Open input and output files
with open(INPUT_FILE, newline='', encoding="utf-8") as infile, open(OUTPUT_FILE, "w", newline='', encoding="utf-8") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    # Read and write the header
    header = next(reader)
    writer.writerow(header)
    outfile.flush()  # Ensure the header is immediately written
    
    # Find column indexes
    key_idx = header.index("Key")
    english_idx = header.index("english")
    lang_indexes = {lang: header.index(lang) for lang in LANGUAGE_MAP}

    # Process each row one at a time
    for row in reader:
        key = row[key_idx]
        english_text = row[english_idx].strip()

        if english_text:
            for lang, lang_code in LANGUAGE_MAP.items():
                lang_idx = lang_indexes[lang]
                
                # Skip already translated entries
                if row[lang_idx].strip():
                    continue  

                try:
                    translation = translator.translate(english_text, src="en", dest=lang_code).text
                    translation = translation.replace(",", " ")  # Remove commas
                    row[lang_idx] = translation
                    
                    # Show progress
                    print(f"Translated '{key}' to {lang}: {translation}")

                    # Delay to avoid being blocked
                    time.sleep(1)

                except Exception as e:
                    print(f"Error translating '{key}' to {lang}: {e}")
                    row[lang_idx] = english_text  # Fallback to English

        # Write the updated row immediately and flush
        writer.writerow(row)
        outfile.flush()

print(f"Translation complete! Output saved to {OUTPUT_FILE}")

