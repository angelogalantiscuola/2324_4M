import os
import re

def rename_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Match the pattern "esercizio_XXX.ext"
            match = re.match(r'(esercizio_)(\d{3})(\..*)', file)
            if match:
                # Remove the first digit from the number part
                new_number = match.group(2)[1:]
                new_filename = f"{match.group(1)}{new_number}{match.group(3)}"
                
                # Get the full paths
                old_file = os.path.join(root, file)
                new_file = os.path.join(root, new_filename)
                
                # Rename the file
                print(f"Renaming {old_file} to {new_file}")
                os.rename(old_file, new_file)

# Call the function with the directory path
rename_files('.')