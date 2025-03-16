# %%
import pandas as pd
import random

# Read the cast_table.csv file
cast_df = pd.read_csv("cast_table.csv")

# Initialize an empty list to store movie_cast records
movie_cast_records = []

# Generate 4832 records
for _ in range(4832):
    # Define the number of cast members to select (between 2 and 4)
    num_cast_members = random.randint(2, 4)
    
    # Select random cast members and sum their salaries
    cast_names = random.sample(cast_df['name'].tolist(), num_cast_members)
    total_cast_expense = sum(cast_df[cast_df['name'].isin(cast_names)]['salary'])
    
    # Create a dictionary for the movie_cast record
    movie_cast_record = {
        'movie_cast_cast_id_1': cast_names[0],
        'movie_cast_cast_id_2': cast_names[1] if len(cast_names) > 1 else '',
        'movie_cast_cast_id_3': cast_names[2] if len(cast_names) > 2 else '',
        'movie_cast_cast_id_4': cast_names[3] if len(cast_names) > 3 else '',
        'movie_cast_total_cast_expense': total_cast_expense
    }
    
    # Append the movie_cast record to the list
    movie_cast_records.append(movie_cast_record)

# Create the movie_cast DataFrame from the list of records
movie_cast_df = pd.DataFrame(movie_cast_records)

# Save the movie_cast DataFrame as a CSV file

# %%
movie_cast_df['movie_cast_id'] = range(1, len(movie_cast_df) + 1)
# Rearrange the columns as per your request
new_column_order = [
    'movie_cast_id',
    'movie_cast_cast_id_1',
    'movie_cast_cast_id_2',
    'movie_cast_cast_id_3',
    'movie_cast_cast_id_4',
    'movie_cast_total_cast_expense'
]
movie_cast_df = movie_cast_df[new_column_order]

# %%
movie_cast_df.head(10)

# %%
movie_cast_df.shape

# %%
# Save the movie_cast DataFrame as a CSV file
movie_cast_df.to_csv("movie_cast.csv", index=False)

# %%
