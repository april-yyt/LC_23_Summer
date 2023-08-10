import os
from datetime import datetime

def generate_files(number_of_files, folder='LC'):
    # Ensure the specified folder exists
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Get the current date in the desired format (MM/DD/YYYY)
    date_str = datetime.today().strftime('%m/%d/%Y')

    # Template for the content of each file
    template = f'''## TOPIC
### Date: {date_str}

# Your solution goes here
'''

    # Iterate from 1 to the number_of_files and create each file
    for i in range(1, number_of_files + 1):
        file_name = f'LC_{i:04}_Problem_Title.py' # You can modify the title as needed
        file_path = os.path.join(folder, file_name)

        with open(file_path, 'w') as file:
            file.write(template)

        print(f'File {file_name} created successfully in {folder} folder.')

# Input for the number of files
number_of_files = int(input("Enter the number of Python files to generate: "))
generate_files(number_of_files)
