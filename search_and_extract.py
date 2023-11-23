import os
import zipfile

def search_and_extract(directory, filename_fragment):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.zip'):
                try:
                    with zipfile.ZipFile(os.path.join(root, file), 'r') as zip_ref:
                        for zip_file in zip_ref.namelist():
                            if filename_fragment in zip_file:
                                print(f"File containing '{filename_fragment}' found in '{file}'")
                                zip_ref.extract(zip_file, path=root)
                                print(f"File '{zip_file}' extracted from '{file}'")
                except Exception as e:
                    print(f"Error processing '{file}': {str(e)}")

# Specify folder and the fragment that contains in file name or full name of a file
search_and_extract('/path/to/directory', 'fragment or filename.txt')