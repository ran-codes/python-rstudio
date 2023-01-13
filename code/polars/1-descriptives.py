import polars as pl
from datetime import date, datetime, timedelta 
import numpy as np 

## Series Creation
series_tuple = pl.Series("a", [1, 2, 3, 4, 5])
series_tuple
series_list = pl.Series([1, 2, 3, 4, 5])
series_list

## Dataframe creation
df = pl.DataFrame(
    {
        "a": [1.0, 2.8, 3.0],
        "b": [4, 5, None],
        "c": [True, False, True],
        "d": [None, "b", "c"],
        "e": ["usd", "eur", None],
        "f": [date(2020, 1, 1), date(2021, 1, 1), date(2022, 1, 1)],
    }
)

####### Descriptives ------------------------------------

## metadata
df.dtypes
df.columns

## operations
df.head(3)
df.tail(3)
df.sample(3)
print(df.glimpse())
df.describe()
df.is_empty()
df.is_unique()
df.n_chunks()


