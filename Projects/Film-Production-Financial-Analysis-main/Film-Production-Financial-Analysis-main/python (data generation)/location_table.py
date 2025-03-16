# %%
import pandas as pd
import random
# Read the location_table.csv file
location_df = pd.read_csv(r"C:\Users\hp\OneDrive - Syracuse University\projects\DBMSData\location_table.csv")

# Determine how many times the records need to be repeated
num_repeats = 4831 // len(location_df) + 1

# Repeat the records and reset the index
repeated_location_df = pd.concat([location_df] * num_repeats, ignore_index=True)

# Add a location_id column starting from 1
repeated_location_df['location_id'] = range(1, len(repeated_location_df) + 1)

# Reorder the columns with location_id as the first column
reordered_columns = ['location_id'] + [col for col in repeated_location_df.columns if col != 'location_id']
repeated_location_df = repeated_location_df[reordered_columns]

# Save the updated DataFrame to a CSV file
repeated_location_df.to_csv("location_table_updated.csv", index=False)
location_table = repeated_location_df.sample(frac=1, random_state=random.seed())

location_table.head(10)
# %%
# Save the updated DataFrame to a CSV file
# Sort the location_df DataFrame by the 'location_id' column

# %%
location_table.to_csv("location_table.csv", index=False)

# %%
