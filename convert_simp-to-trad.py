# install opencc-python before runing this script
# pip install opencc-python-reimplemented


from opencc import OpenCC

# Initialize OpenCC for Simplified-to-Traditional conversion
converter = OpenCC('s2t')

# Prompt user for file paths
input_file = input("Enter the path to your input file (Simplified Chinese): ")
output_file = input("Enter the path to save the output file (Traditional Chinese): ")

# Read, convert, and save the file
try:
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    converted_content = converter.convert(content)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(converted_content)

    print("Conversion complete. The file is saved as:", output_file)

except FileNotFoundError:
    print("The specified file was not found. Please check the file path and try again.")
except Exception as e:
    print("An error occurred:", e)

