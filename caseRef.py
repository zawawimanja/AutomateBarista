html_content = """
<select class="input-xs" name="custom_field_18[]">
    <option value="1715831751306 ">1715831751306 </option>
    <option value="249094">249094</option>
 <option value="800908025781 ">800908025781 </option>
</select>
"""

# Extract option values
import re
option_values = re.findall(r'value="\s*(\d+)\s*"', html_content)

# Print all extracted values
print("Extracted values:", option_values)
