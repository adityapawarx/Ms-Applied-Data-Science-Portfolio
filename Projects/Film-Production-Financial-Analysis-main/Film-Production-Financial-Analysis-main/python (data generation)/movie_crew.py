# %%
import pandas as pd
import random

# Read the crew_table.csv file
crew_df = pd.read_csv(r"C:\Users\hp\OneDrive - Syracuse University\projects\DBMSData\crew_table.csv")

# Initialize an empty list to store movie_crew records
movie_crew_records = []

# Generate 4833 records
for movie_crew_id in range(1, 4834):
    # Choose a random number of crew members between 3 and 6
    num_crew_members = random.randint(3, 6)
    
    # Randomly select crew members and sum their salaries
    crew_selection = random.sample(list(crew_df.index), num_crew_members)
    selected_crew = crew_df.iloc[crew_selection]
    total_crew_expense = selected_crew['Salary'].sum()
    
    # Create a dictionary for the movie_crew record
    movie_crew_record = {'movie_crew_id': movie_crew_id, 'movie_crew_total_expense': total_crew_expense}
    
    # Add crew names and salaries to the dictionary with prefixes
    for i in range(num_crew_members):
        crew_name_column = f'movie_crew_name_{i+1}'
        crew_salary_column = f'movie_crew_salary_{i+1}'
        
        if i < len(selected_crew):
            movie_crew_record[crew_name_column] = selected_crew.iloc[i]['Crew Type']
            movie_crew_record[crew_salary_column] = selected_crew.iloc[i]['Salary']
        else:
            movie_crew_record[crew_name_column] = None
            movie_crew_record[crew_salary_column] = None
    
    # Append the movie_crew record to the list
    movie_crew_records.append(movie_crew_record)

# Create the movie_crew DataFrame from the list of records
movie_crew_df = pd.DataFrame(movie_crew_records)

# Save the movie_crew DataFrame as a CSV file
movie_crew_df.to_csv("movie_crew.csv", index=False)

# %%

movie_crew_df.head(50)
# %%


# %%


# %%


# %%


# %%


