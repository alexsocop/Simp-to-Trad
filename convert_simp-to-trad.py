# install opencc-python before runing this script
# pip install opencc-python-reimplemented


import os
from opencc import OpenCC

# Initialize OpenCC for Simplified-to-Traditional conversion
converter = OpenCC('s2t')

# Prompt user for input file path
input_file = input("Enter the path to your input file (Simplified Chinese): ")

# Automatically create output file name in the same directory
input_dir = os.path.dirname(input_file)
base_name = os.path.basename(input_file)
name, ext = os.path.splitext(base_name)
output_file = os.path.join(input_dir, f"{name}_ZH-TW{ext}")

# Read, convert, and save the file
try:
    try:
        # Try reading as UTF-8 first
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # Fallback to UTF-16 if UTF-8 fails
        with open(input_file, 'r', encoding='utf-16') as f:
            content = f.read()

    converted_content = converter.convert(content)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(converted_content)

    print("Conversion complete. The file is saved as:", output_file)

except FileNotFoundError:
    print("The specified file was not found. Please check the file path and try again.")
except Exception as e:
    print("An error occurred:", e)
