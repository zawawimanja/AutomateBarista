# Read HTML content from a file
with open('caseRef.html', 'r') as file:
    html_content = file.read()

# Extract option values using a regex that matches both numeric and alphanumeric values
import re
option_values_raw = re.findall(r'value="\s*([A-Za-z0-9,]+)\s*"', html_content)

# Split combined values into individual values
option_values = []
for value in option_values_raw:
    option_values.extend(value.split(','))

# List of input values to check
input_values = [
    "B32NTO20240000018",
    "B34NTO20240000022",
    "B32NTO20240000025",
    "B32NTO20240000027",
    "B32NTO20240000032",
    "A31NTI20240000145",
    "A31NTI20240000156",
    "A31NTI20240000165",
    "A31NTI20240000164",
    "A31NTI20240000196",
    "A31NTI20240000199",
    "A31NTI20240000200",
    "A31NTI20240000198",
    "A31NTI20240000201",
    "A31NTI20240000218",
    "A31NTI20240000228",
    "A31NTI20240000250",
    "A31NTI20240000266"
]

# Lists to store values that exist and do not exist
exist_values = []
not_exist_values = []

# Check if each input value exists in the extracted option values
for value in input_values:
    if value in option_values:
        exist_values.append(value)
    else:
        not_exist_values.append(value)

# Function to print the values in groups
def print_in_groups(values, group_name):
    print(f"\n{group_name} ({len(values)} items):")
    for i in range(0, len(values), 5):
        group = values[i:i + 5]
        print(", ".join(group))

# Print the results
print_in_groups(exist_values, "Exist")
print_in_groups(not_exist_values, "Not Exist")
