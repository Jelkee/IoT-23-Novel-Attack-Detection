import os
import pandas as pd
from tqdm import tqdm

# Directory containing the malware CSV files
malware_dir = 'malware'

# Output file where the combined data will be saved
output_file = 'malware_combined.csv'

# Get the list of all CSV files in the malware directory
file_paths = [os.path.join(malware_dir, f) for f in os.listdir(malware_dir) if f.endswith('.csv')]

# Initialize the output file by writing the header
first_file = True

for file_path in tqdm(file_paths):
    print(f"Processing {file_path}")
    # Read the CSV file in chunks
    for chunk in pd.read_csv(file_path, chunksize=100000, dtype='str'):
        # Append chunk to the output file
        if first_file:
            chunk.to_csv(output_file, mode='w', header=True, index=False)
            first_file = False
        else:
            chunk.to_csv(output_file, mode='a', header=False, index=False)

print("All files have been concatenated and written to", output_file)
