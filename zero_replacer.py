import pandas as pd

input_file_path = 'honey_optimized/honey4optimized.csv'  # Change this to your input file path
output_file_path = 'honey_optimized/honey4optimized.csv'  # Change this to your desired output file path

df = pd.read_csv(input_file_path)

df['label'] = df['label'].fillna(0)
df['label'] = df['label'].apply(lambda x: int(x) if isinstance(x, float) else x)

df.to_csv(output_file_path, index=False)
