# %%
import pandas as pd
import numpy as np
# %%
# Assuming df is your original DataFrame
df_RAW_director = pd.read_csv("RAW_top_directors_data.csv")
df_RAW_director.columns
# %%
df_RAW_director=df_RAW_director[['title', 'director', 'genres']]
df_RAW_director.columns

# %%
df_RAW_movies = pd.read_csv("Raw_top_movie_data.csv")
df_RAW_movies.columns

# %%
df_RAW_movies = df_RAW_movies[['title', 'directors', 'genres','budget']]

# %%
df_RAW_movies.rename(columns={'directors': 'director'}, inplace=True)


df_RAW_movies.head(2)
# %%
df_RAW_movies.columns
# %%
df_RAW_director.columns
# %%
df_RAW = pd.concat([df_RAW_movies, df_RAW_director], ignore_index=True)
df_RAW.tail(3)
# %%
df_RAW = df_RAW.rename(columns={'title':'movie_name', 'director':'director_name',
                       'genres':'movie_genres','budget':'movie_budget'})
# %%
df_RAW['movie_id'] = np.arange(1, len(df_RAW) + 1)
df_RAW.head(5)
# %%# %%
df_RAW['movie_producer_id'] = np.nan
df_RAW['movie_expense_id'] = np.nan
df_RAW['movie_director_id'] = np.nan

# Reorder columns
df_RAW = df_RAW[['movie_id', 'movie_name', 'movie_genres', 'movie_budget',
                 'movie_producer_id', 'movie_expense_id', 'movie_director_id', 'director_name']]

# Display the DataFrame
df_RAW.tail(1)
# %%
#DIRECTORS TABLE UNDER CREATION

# First, create director_table
director_table = df_RAW[['director_name']].drop_duplicates().reset_index(drop=True)
director_table['director_id'] = np.arange(1, len(director_table) + 1)
director_table.head(3)
# %%
# Now, update df_RAW with director IDs
df_RAW = df_RAW.merge(director_table, on='director_name', how='left')
df_RAW.head(3)
# %%
df_RAW.drop(columns=['movie_director_id', 'director_name', 'director_id_x'], inplace=True)
df_RAW.rename(columns={'director_id_y': 'movie_director_id'}, inplace=True)
df_RAW.to_csv("movie_table.csv", index=False)
director_table.to_csv("director_table.csv", index=False)


# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
