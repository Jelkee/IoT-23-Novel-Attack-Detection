import csv
from collections import Counter


def count_column_values(csv_file_path, column_index):
    # Initialize a Counter object to store the count of each value
    counter = Counter()

    try:
        # Open the CSV file
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            # Create a CSV reader object
            csvreader = csv.reader(csvfile)

            # Iterate through each row in the CSV file
            for row in csvreader:
                # Ensure the row has enough columns
                if len(row) > column_index:
                    # Get the value from the specified column
                    value = row[column_index]
                    # Update the counter with the value
                    counter[value] += 1
                else:
                    print(f"Row has fewer than {column_index + 1} columns: {row}")

        return counter
    except FileNotFoundError:
        print(f"File not found: {csv_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Path to the CSV file
    csv_file_path = 'honey/honey7.csv'
    column_index = 22

    # Get the count of values in the specified column
    value_counts = count_column_values(csv_file_path, column_index)

    # Print the results
    if value_counts:
        print("Value counts in column 22:")
        for value, count in value_counts.items():
            print(f"{value}: {count}")
