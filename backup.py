import os
import shutil
from datetime import datetime 

def copy_files(s_d, d_d):
    try:
        if not os.path.exists(s_d): #checking if exists
            raise FileNotFoundError(f"Source directory '{s_d}' not found.")

        if not os.path.exists(d_d): #if not creates it
            os.makedirs(d_d)

        for filename in os.listdir(s_d): #loop for every file
            source_filepath = os.path.join(s_d, filename)
            destination_filepath = os.path.join(d_d, filename)

            shutil.copy2(source_filepath, destination_filepath) # copying the file
            print(f"File '{filename}' copied to '{d_d}'")

        print("All files copied successfully.")

    except Exception as e:
        print(f"Error: {e}")

# Example usage:
s_d = r"C:\Users\chviv\Desktop\Hero Vired - Python Assignements (vcheruku)\Source"
d_d = r"C:\Users\chviv\Desktop\Hero Vired - Python Assignements (vcheruku)\Destination"

copy_files(s_d, d_d)
