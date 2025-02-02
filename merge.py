import json

# List to hold merged data
merged_data = []

# Loop through files from data1.json to data12.json
for i in range(1, 13):
    filename = f"data{i}.json"
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            # Wrap data in {} and append to the merged list
            data["index_id"] = f"{i}"
            merged_data.append(data)
    except FileNotFoundError:
        print(f"{filename} not found. Skipping...")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in {filename}. Skipping...")

# Write merged data to a new JSON file
with open('merged_data.json', 'w') as outfile:
    json.dump(merged_data, outfile, indent=4)

print("Merging complete. Data saved in merged_data.json")