import json
"""
# Load the JSON files
file1 = 'C:/NLP/Final Project/fp-dataset-artifacts-main/eval_output_72/eval_predictions.jsonl'
file2 = 'C:/NLP/Final Project/fp-dataset-artifacts-main/fine_tuning_data.json'
with open(file1, 'r') as f1, open(file2, 'r') as f2:
    data1 = json.load(f1)  # Load first file
    data2 = json.load(f2)  # Load second file

# Combine the lists
merged_data = data1 + data2

# Write the merged data to a new JSON file
with open('merged_file.json', 'w') as outfile:
    json.dump(merged_data, outfile, indent=4)

"""

"""
import json
# Fileter the data where label and prediction won't match.
# File paths
input_file = 'eval_output_52\eval_predictions.jsonl'  # Replace with your input file path
output_file = 'filtered_data.json'  # Output file path

# Initialize an empty list to hold the filtered data
filtered_data = []

# Read the JSONL file line by line
with open(input_file, 'r') as f:
    for line in f:
        # Parse each line as a JSON object
        entry = json.loads(line)

        # Check if the 'label' is not equal to 'predicted_label'
        if entry['label'] != entry['predicted_label']:
            filtered_data.append(entry)

# Save the filtered data as a JSON file
with open(output_file, 'w') as f:
    json.dump(filtered_data, f, indent=4)

print(f"Filtered data saved to {output_file}")

"""

"""
import json
# Fileter the data where label and prediction won't match.
# File paths
input_file = 'eval_output_52\eval_predictions.jsonl'  # Replace with your input file path
output_file = 'filtered_data_label_1.jsonl'  # Output file path

# Initialize an empty list to hold the filtered data
filtered_data = []

with open(input_file, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
    buffer = []
    for line in f_in:
        line = line.strip()
        if line.startswith("{") or len(buffer) > 0:  # Start of a JSON object or continuation
            buffer.append(line)
            if line.endswith("}"):  # End of a JSON object
                try:
                    # Join lines to form a complete JSON object and validate it
                    complete_object = " ".join(buffer)
                    json.loads(complete_object)  # Validate JSON
                    f_out.write(complete_object + "\n")  # Write valid JSON object to output
                except json.JSONDecodeError:
                    print(f"Skipping invalid JSON object: {buffer}")
                buffer = []  # Clear buffer for the next object
        else:
            print(f"Skipping invalid line: {line}")

print(f"Fixed JSONL file saved to {output_file}")
"""
""""
import json
# Fileter the data where label and prediction won't match.
# File paths
input_file = 'eval_output_52\eval_predictions.jsonl'  # Replace with your input file path
output_file = 'filtered_label1.json'  # Output file path

# Initialize an empty list to hold the filtered data
filtered_data = []

# Read the JSONL file line by line
with open(input_file, 'r') as f:
    for line in f:
        # Parse each line as a JSON object
        data = json.loads(line)

        # Check if the 'label' is not equal to 'predicted_label'
        if data['label'] != data['predicted_label']:
            # Remove 'similarity_score' and 'predicted_scores' from the data
            data_filtered = {key: data[key] for key in data if key not in ['similarity_score', 'predicted_scores']}
            filtered_data.append(data_filtered)

# Save the filtered data as a JSON file
with open(output_file, 'w') as outfile:
    json.dump(filtered_data, outfile, indent=4)

print(f"Filtered data saved to {output_file}")

"""
""""
import json
# Fileter the data where label and prediction won't match.
# File paths
input_file = 'eval_output_52\eval_predictions.jsonl'  # Replace with input file path
output_file = 'filtered_label11.jsonl'  # Output file path

# Initialize an empty list to hold the filtered data
filtered_data = []

with open(input_file, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
    buffer = []
    for line in f_in:
        line = line.strip()
        if line.startswith("{") or len(buffer) > 0:  # Start of a JSON object or continuation
            buffer.append(line)
            if line.endswith("}"):  # End of a JSON object
                try:
                    # Join lines to form a complete JSON object and validate it
                    complete_object = " ".join(buffer)
                    json.loads(complete_object)  # Validate JSON
                    f_out.write(complete_object + "\n")  # Write valid JSON object to output
                except json.JSONDecodeError:
                    print(f"Skipping invalid JSON object: {buffer}")
                buffer = []  # Clear buffer for the next object
        else:
            print(f"Skipping invalid line: {line}")

print(f"Fixed JSONL file saved to {output_file}")
"""

"""
import pandas as pd

# Path to your JSONL file
input_file = 'filtered_data_label_1.jsonl'
output_file = 'output_x.xlsx'

# Open the file and read each line
data = []
with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            # Parse each line as JSON
            data.append(json.loads(line))
        except json.JSONDecodeError:
            print(f"Skipping invalid line: {line.strip()}")  # Skip lines that are not valid JSON

# Check if data was successfully loaded
if len(data) == 0:
    raise ValueError("No valid JSON lines found in the file!")

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel(output_file, index=False, engine='openpyxl')

print(f"Excel file saved as {output_file}")
"""
"""
import json
# Fileter the data where label and prediction won't match.
# File paths
input_file = 'eval_output_52\eval_predictions.jsonl'  # Replace with your input file path
output_file = 'filtered_1_0.json'  # Output file path

# Initialize an empty list to hold the filtered data
filtered_data = []

# Read the JSONL file line by line
with open(input_file, 'r') as f:
    for line in f:
        # Parse each line as a JSON object
        data = json.loads(line)

        # Check if the 'label' is not equal to 'predicted_label'
        if data['label'] == 1 and data['predicted_label'] == 0:
            # Remove 'similarity_score' and 'predicted_scores' from the data
            data_filtered = {key: data[key] for key in data if key not in ['similarity_score', 'predicted_scores']}
            filtered_data.append(data_filtered)

# Save the filtered data as a JSON file
with open(output_file, 'w') as outfile:
    json.dump(filtered_data, outfile, indent=4)

print(f"Filtered data saved to {output_file}")
"""

# create adv data for label 1 and 0
# advesarial_data_L1_with_0.json
import json
# Fileter the data where label and prediction won't match.
# File paths
input_file = 'eval_output_52\eval_predictions.jsonl'  # Replace with your input file path
output_file = 'advesarial_data_L1_with_0.json'  # Output file path

# Initialize an empty list to hold the filtered data
filtered_data = []

# Read the JSONL file line by line
with open(input_file, 'r') as f:
    for line in f:
        # Parse each line as a JSON object
        data = json.loads(line)

        # Check if the 'label' is not equal to 'predicted_label'
        if data['label'] == 1 and data['predicted_label'] == 0:
            # Remove 'similarity_score' and 'predicted_scores' from the data
            data_filtered = {key: data[key] for key in data if key not in ['similarity_score', 'predicted_scores']}
            filtered_data.append(data_filtered)

# Save the filtered data as a JSON file
with open(output_file, 'w') as outfile:
    json.dump(filtered_data, outfile, indent=4)

print(f"Filtered data saved to {output_file}")

""""
# create adv data for label 1 and 2
# advesarial_data_L1_with_2.json
import json
# Fileter the data where label and prediction won't match.
# File paths
input_file = 'eval_output_52\eval_predictions.jsonl'  # Replace with your input file path
output_file = 'advesarial_data_L1_with_2.json'  # Output file path

# Initialize an empty list to hold the filtered data
filtered_data = []

# Read the JSONL file line by line
with open(input_file, 'r') as f:
    for line in f:
        # Parse each line as a JSON object
        data = json.loads(line)

        # Check if the 'label' is not equal to 'predicted_label'
        if data['label'] == 1 and data['predicted_label'] == 0:
            # Remove 'similarity_score' and 'predicted_scores' from the data
            data_filtered = {key: data[key] for key in data if key not in ['similarity_score', 'predicted_scores']}
            filtered_data.append(data_filtered)

# Save the filtered data as a JSON file
with open(output_file, 'w') as outfile:
    json.dump(filtered_data, outfile, indent=4)

print(f"Filtered data saved to {output_file}")

"""
"""
import json

# Specify the path to your JSON file
json_file_path = 'advesarial_data_L1_with_0 - Copy.json'

# Open the file and load the current data
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Empty the data (if it's a list or dictionary)
data.clear()

# Save the empty data back to the file
with open(json_file_path, 'w') as file:
    json.dump(data, file, indent=4)

print("All entries deleted from the JSON file.")

"""
"""
# convert a json to jsonl
import json

# Load the JSON data (assuming it's a list of dictionaries)
with open('advesarial_data_L_1_with_0.json', 'r') as json_file:

    data = json.load(json_file)

output_file = 'advesarial_data_L_1_with_0.jsonl'
with open(output_file, 'w') as jsonl_file:
    for entry in data:
        jsonl_file.write(json.dumps(entry) + '\n')
"""


