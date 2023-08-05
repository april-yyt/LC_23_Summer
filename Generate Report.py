import os
import re
import pandas as pd

# store extracted info in a list of dictionaries
data = []

# walk through the directory
for root, dirs, files in os.walk('.'):
    # iterate over each file
    for filename in files:
        # check if it is a .py file and starts with 'LC'
        if filename.endswith('.py') and filename.startswith('LC'):
            # get the relative path from the root to the file
            file_path = os.path.join(root, filename)
            # open and read the file
            with open(file_path, 'r') as file:
                content = file.read()

            # extract information
            lc_id, lc_name = filename[3:-3].split('_')
            topics = re.findall('^## (.*)$', content, re.MULTILINE)
            date = re.search('### Date: (.*)$', content, re.MULTILINE).group(1)
            
            # Get category from root directory structure
            category = os.path.basename(root)

            # store the info
            data.append({
                'ID': lc_id,
                'Name': lc_name.replace('_', ' '),
                'Topic': ', '.join(topics),
                'Date': date,
                'Category': category  # add 'Category' field
            })

# create a dataframe
df = pd.DataFrame(data)

# convert 'Date' column to datetime format and sort by date in descending order
df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%m/%d/%Y')
df = df.sort_values('Date', ascending=False)

# write dataframe to README.md
with open('README.md', 'w') as f:
    f.write(df.to_markdown(index=False))
