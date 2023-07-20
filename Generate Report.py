import os
import re
import pandas as pd

# store extracted info in a list of dictionaries
data = []

# list files in current directory
for filename in os.listdir('.'):
    # check if it is a .py file and starts with 'LC'
    if filename.endswith('.py') and filename.startswith('LC'):
        # open and read the file
        with open(filename, 'r') as file:
            content = file.read()

        # extract information
        lc_id, lc_name = filename[3:-3].split('_')
        topics = re.findall('^## (.*)$', content, re.MULTILINE)
        date = re.search('### Date: (.*)$', content, re.MULTILINE).group(1)
        # company = re.search('#### (.*)$', content, re.MULTILINE).group(1)
        # tc_sc = re.findall('^## (TC|SC): (.*)$', content, re.MULTILINE)

        # store the info
        data.append({
            'ID': lc_id,
            'Name': lc_name.replace('_', ' '),
            'Topic': ', '.join(topics),
            'Date': date,
            # 'Company': company,
            # 'Time Complexity': tc_sc[0][1] if tc_sc[0][0] == 'TC' else tc_sc[1][1],
            # 'Space Complexity': tc_sc[0][1] if tc_sc[0][0] == 'SC' else tc_sc[1][1]
        })

# create a dataframe
df = pd.DataFrame(data)

# convert 'Date' column to datetime format and sort by date in descending order
df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%m/%d/%Y')
df = df.sort_values('Date', ascending=False)

# write dataframe to README.md
with open('README.md', 'w') as f:
    f.write(df.to_markdown(index=False))
