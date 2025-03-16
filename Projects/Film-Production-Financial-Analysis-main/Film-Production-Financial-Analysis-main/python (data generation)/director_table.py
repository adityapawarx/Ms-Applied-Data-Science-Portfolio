# %%
import pandas as pd
import numpy as np
# %%
df = pd.read_csv("top_directors_data.csv")
# %%
df.columns

# %%
df = df[["index", "director"]]
# %%
df.head(30)
# %%
df.to_csv("directors_table.csv", index=False)

# %%


# %%


# %%


# %%


# %%


# %%


