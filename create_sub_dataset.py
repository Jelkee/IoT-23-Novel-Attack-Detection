import pandas as pd
from tqdm import tqdm

# Path to the large dataset
large_dataset_path = 'fileshuffle_malware_combined.csv'
# Path to save the test set
path_0 = 'filtered/detailed_label_0.csv'
path_2 = 'filtered/detailed_label_2.csv'
path_3 = 'filtered/detailed_label_3.csv'
path_4 = 'filtered/detailed_label_4.csv'
path_5 = 'filtered/detailed_label_5.csv'
path_6 = 'filtered/detailed_label_6.csv'
path_7 = 'filtered/detailed_label_7.csv'
path_8 = 'filtered/detailed_label_8.csv'
path_9 = 'filtered/detailed_label_9.csv'
# Define chunk size
chunk_size = 3000000

# Create an empty DataFrame to store the test set
test_set_0 = pd.DataFrame()
test_set_2 = pd.DataFrame()
test_set_3 = pd.DataFrame()
test_set_4 = pd.DataFrame()
test_set_5 = pd.DataFrame()
test_set_6 = pd.DataFrame()
test_set_7 = pd.DataFrame()
test_set_8 = pd.DataFrame()
test_set_9 = pd.DataFrame()

header_written_0 = False

# Iterate over the large dataset in chunks
for chunk in tqdm(pd.read_csv(large_dataset_path, chunksize=chunk_size)):
    filtered_chunk_0 = chunk[chunk.iloc[:, -1] == 0]
    #filtered_chunk_2 = chunk[chunk.iloc[:, -1] == 2]
    #filtered_chunk_3 = chunk[chunk.iloc[:, -1] == 3]
    #filtered_chunk_4 = chunk[chunk.iloc[:, -1] == 4]
    #filtered_chunk_5 = chunk[chunk.iloc[:, -1] == 5]
    #filtered_chunk_6 = chunk[chunk.iloc[:, -1] == 6]
    #filtered_chunk_7 = chunk[chunk.iloc[:, -1] == 7]
    #filtered_chunk_8 = chunk[chunk.iloc[:, -1] == 8]
    #filtered_chunk_9 = chunk[chunk.iloc[:, -1] == 9]

    test_set_0 = pd.concat([test_set_0, filtered_chunk_0], ignore_index=True)
    #test_set_2 = pd.concat([test_set_2, filtered_chunk_2], ignore_index=True)
    #test_set_3 = pd.concat([test_set_3, filtered_chunk_3], ignore_index=True)
    #test_set_4 = pd.concat([test_set_4, filtered_chunk_4], ignore_index=True)
    #test_set_5 = pd.concat([test_set_5, filtered_chunk_5], ignore_index=True)
    #test_set_6 = pd.concat([test_set_6, filtered_chunk_6], ignore_index=True)
    #test_set_7 = pd.concat([test_set_7, filtered_chunk_7], ignore_index=True)
    # if not filtered_chunk_0.empty:
    #     filtered_chunk_0.to_csv(path_8, mode='a', header=not header_written_8, index=False)
    #     header_written_8 = True
    #test_set_9 = pd.concat([test_set_9, filtered_chunk_9], ignore_index=True)


# Save the test set to a CSV file
test_set_0.to_csv(path_0, index=False)
#test_set_3.to_csv(path_3, index=False)
#test_set_4.to_csv(path_4, index=False)
#test_set_5.to_csv(path_5, index=False)
#test_set_6.to_csv(path_6, index=False)
#test_set_7.to_csv(path_7, index=False)
#test_set_8.to_csv(path_8, index=False)
#test_set_9.to_csv(path_9, index=False)

