
#THIS FILE IS USED TO SPLIT LARGE LABELED FILES INTO MULTIPLE PARTS FOR MEMORY EFFICIENCY. NOTE THAT THE HEADERS NEED TO BE ADDED MANUALLY AFTER

import os
def split_file(input_file, num_parts):
    file_size = os.path.getsize(input_file)
    part_size = file_size // num_parts
    remainder = file_size % num_parts

    with open(input_file, 'rb') as f:
        for i in range(num_parts):
            part_file_name = f"{input_file}_part{i + 1}"
            with open(part_file_name, 'wb') as part_file:
                # For each part, read part_size bytes (add remainder to the last part)
                if i == num_parts - 1:
                    part_file.write(f.read(part_size + remainder))
                else:
                    part_file.write(f.read(part_size))
            print(f"Created: {part_file_name}")


if __name__ == "__main__":
    input_file = "labeled_files/conn.log.labeled"
    num_parts = 5

    split_file(input_file, num_parts)
