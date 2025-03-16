# %%
import pandas as pd
import numpy as np
# %%
a=pd.read_csv("C:/Users/hp/OneDrive - Syracuse University/projects/DBMSData/Database/final/Final first 1000 rows/director_table.csv")
b=pd.read_csv("C:/Users/hp/OneDrive - Syracuse University/projects/DBMSData/Database/final/Final first 1000 rows/expense_table.csv")
c=pd.read_csv("C:/Users/hp/OneDrive - Syracuse University/projects/DBMSData/Database/final/Final first 1000 rows/location_table.csv")
d=pd.read_csv("C:/Users/hp/OneDrive - Syracuse University/projects/DBMSData/Database/final/Final first 1000 rows/movie_cast.csv")
e=pd.read_csv("C:/Users/hp/OneDrive - Syracuse University/projects/DBMSData/Database/final/Final first 1000 rows/movie_crew.csv")
f=pd.read_csv("C:/Users/hp/OneDrive - Syracuse University/projects/DBMSData/Database/final/Final first 1000 rows/movie_table_updated.csv")
g=pd.read_csv("C:/Users/hp/OneDrive - Syracuse University/projects/DBMSData/Database/final/Final first 1000 rows/producer_table.csv")
# %%
# Assuming a, b, c, d, e, f, g are already defined dataframes
a = a.head(1000)
b = b.head(1000)
c = c.head(1000)
d = d.head(1000)
e = e.head(1000)
f = f.head(1000)
g = g.head(1000)


# %%
a.to_csv("C:/Users/hp/OneDrive - Syracuse University/projects/DBMSData/Database/final/Final first 1000 rows/director_table_trimmed.csv", index=False)
b.to_csv("C:/Users/hp/OneDrive - Syracuse University/projects/DBMSData/Database/final/Final first 1000 rows/expense_table_trimmed.csv", index=False)
c.to_csv("C:/Users/hp/OneDrive - Syracuse University/projects/DBMSData/Database/final/Final first 1000 rows/location_table_trimmed.csv", index=False)
d.to_csv("C:/Users/hp/OneDrive - Syracuse University/projects/DBMSData/Database/final/Final first 1000 rows/movie_cast_trimmed.csv", index=False)
e.to_csv("C:/Users/hp/OneDrive - Syracuse University/projects/DBMSData/Database/final/Final first 1000 rows/movie_crew_trimmed.csv", index=False)
f.to_csv("C:/Users/hp/OneDrive - Syracuse University/projects/DBMSData/Database/final/Final first 1000 rows/movie_table_updated_trimmed.csv", index=False)
g.to_csv("C:/Users/hp/OneDrive - Syracuse University/projects/DBMSData/Database/final/Final first 1000 rows/producer_table_trimmed.csv", index=False)

# %%
