
#%%
import pandas as pd

# Read the necessary tables
producer_table = pd.read_csv(r"C:\Users\hp\OneDrive - Syracuse University\projects\DBMSData\Database\producer_table.csv")
expense_table = pd.read_csv(r"C:\Users\hp\OneDrive - Syracuse University\projects\DBMSData\Database\expense_table.csv")
movie_table = pd.read_csv("movie_table.csv")

# Determine the number of times to repeat producer IDs
num_producer_ids_needed = len(movie_table)
num_producer_repeats = num_producer_ids_needed // len(producer_table) + 1

# Repeat producer IDs to fill movie_producer_id column
producer_ids = producer_table['producer_id'].tolist()
movie_table['movie_producer_id'] = (producer_ids * num_producer_repeats)[:num_producer_ids_needed]

# Take the first 4831 expense IDs to fill movie_expense_id column
expense_ids = expense_table['expense_id'].tolist()[:4831]
movie_table['movie_expense_id'] = expense_ids[:num_producer_ids_needed]

# Save the updated movie_table

#%%
movie_table
#%%

movie_table.to_csv("movie_table_updated.csv", index=False)

#%%

#%%

#%%

