# The input string with no new lines
input_string = """
--------------
id | salary
--------------
1  | 9000
2  | 6000
3  | 7000
--------------
"""

# Split the string into lines and filter out the separators and headers
lines = input_string.strip().split('\n')

# Initialize a list to hold tuples of (id, salary)
data = []

# Iterate over each segment and process
for line in lines[2:]:
    if '|' in line and line != '--------------':
        parts = line.split('|')
        id = int(parts[0].strip())
        salary = int(parts[1].strip())
        data.append((id, salary))

# Find the id with the maximum salary
max_id, max_salary = max(data, key=lambda x: x[1])

print(f"ID: {max_id}, Max Salary: {max_salary}")
