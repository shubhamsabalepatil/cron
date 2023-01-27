# Importing the required libraries
import psutil
import datetime
import pandas as pd

# Creating lists to store the corresponding information

pids = []
status = []

# Getting application process information using psutil
for process in psutil.process_iter():
    pids.append(process.pid)
    status.append(process.status())

# Saving the process information in a python dictionary
data = {"PIds": pids,
        "Status": status,
        }

# Converting the dictionary into Pandas DataFrame
process_df = pd.DataFrame(data)

# Setting the index to pids
process_df = process_df.set_index("PIds")


print(process_df)