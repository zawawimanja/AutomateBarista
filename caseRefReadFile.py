# Read HTML content from a file
with open("caseRef.html", "r") as file:
    html_content = file.read()

# Extract option values using a regex that matches both numeric and alphanumeric values
import re

option_values_raw = re.findall(r'value="\s*([A-Za-z0-9,]+)\s*"', html_content)

# Split combined values into individual values
option_values = []
for value in option_values_raw:
    option_values.extend(value.split(","))

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
    "A31NTI20240000266",
]

# Check if each input value exists in the extracted option values
for value in input_values:
    if value in option_values:
        print(f"{value} exists in the options.")
    else:
        print(f"{value} does not exist in the options.")
