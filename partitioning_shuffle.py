#This file was used to shuffle large csv files without having sufficient memory. This was not used in the final tests.


import pandas as pd
import os
import random
from tempfile import TemporaryDirectory


file_path = 'malware_combined.csv'
output_path = 'fileshuffle_malware_combined.csv'


chunk_size = 1000000


temp_files = []


with TemporaryDirectory() as temp_dir:
    for i, chunk in enumerate(pd.read_csv(file_path, chunksize=chunk_size,
                                          dtype={'conn_state': 'float64', 'service': 'float64'})):
        temp_file_path = os.path.join(temp_dir, f'temp_{i}.csv')
        chunk.to_csv(temp_file_path, index=False)
        temp_files.append(temp_file_path)


    random.shuffle(temp_files)


    with open(output_path, 'w') as output_file:

        with open(temp_files[0], 'r') as temp_file:
            output_file.write(temp_file.readline())

        for temp_file_path in temp_files:
            with open(temp_file_path, 'r') as temp_file:
                next(temp_file)  # Skip header
                for line in temp_file:
                    output_file.write(line)

