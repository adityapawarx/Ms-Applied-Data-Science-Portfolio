# %%
import pandas as pd
import numpy as np
# %%

# Read the necessary tables
cast_df = pd.read_csv("movie_cast.csv")
location_df = pd.read_csv("location_table.csv")
movie_crew_df = pd.read_csv("movie_crew.csv")

# Calculate expenses for location, movie_cast, and movie_crew
location_expenses = location_df['location_cost'].sum()
movie_cast_expenses = cast_df['movie_cast_total_cast_expense'].sum()
movie_crew_expenses = movie_crew_df[['movie_crew_salary_1', 'movie_crew_salary_2', 'movie_crew_salary_3', 'movie_crew_salary_4', 'movie_crew_salary_5', 'movie_crew_salary_6']].sum(axis=1)

# Create expense_table DataFrame with the shorter length
expense_table = pd.DataFrame({
    'expense_id': list(range(1, len(location_df) + 1)),
    'expence_location_id': np.random.choice(location_df['location_id'], len(location_df)),  # Random location IDs
    'expense_movie_cast_id': np.random.choice(cast_df['movie_cast_id'], len(location_df)),  # Random movie_cast IDs
    'expense_movie_crew_id': np.random.choice(movie_crew_df['movie_crew_id'], len(location_df))  # Random movie_crew IDs
})

# Add the longer series with NaNs for the extra values
expense_table['expense_total'] = pd.Series(location_expenses + movie_cast_expenses + movie_crew_expenses)


# %%

expense_table.head(5)
# %%
# Save the expense_table as a CSV file
expense_table.to_csv("expense_table.csv", index=False)

# Save the expense_table as a CSV file
# %%
expense_table
# %%
expense_table.to_csv("expense_table.csv", index=False)


# %%


# %%


