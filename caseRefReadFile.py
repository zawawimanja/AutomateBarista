# Read HTML content from a file
with open('caseRef.html', 'r') as file:
    html_content = file.read()

# Extract option values using a regex that matches both numeric and alphanumeric values
import re
option_values = re.findall(r'value="\s*([A-Za-z0-9]+)\s*"', html_content)

# Print all extracted values
print("Extracted values:", option_values)
