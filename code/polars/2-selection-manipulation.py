##### Setup ---------------------------------------
import polars as pl
from datetime import datetime, timedelta 
import numpy as np 
import seaborn as sns
df = pl.from_pandas(sns.load_dataset('penguins') )


##### Manipulation/Selection  ---------------------------------------
df = pl.read_csv( "https://gist.githubusercontent.com/ritchie46/cac6b337ea52281aa23c049250a4ff03/raw/89a957ff3919d90e6ef2d34235e6bf22304f3366/pokemon.csv").to_pandas()
## filter()
dfa = pl.DataFrame(
    {
        "foo": [1, 2, 3],
        "bar": [6, 7, 8],
        "ham": ["a", "b", "c"],
    }
)
dfa.filter(pl.col("foo") < 3)

## drop_na()
df.drop_nulls()

## row_bind()
dfa = pl.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})
dfb = pl.DataFrame({"foo": [10, 20, 30], "bar": [40, 50, 60]})
dfa.extend(dfb)

## replace_na()
dfa = pl.DataFrame(
    {
        "a": [1.5, 2, float("NaN"), 4],
        "b": [0.5, 4, float("NaN"), 13],
    }
)
dfa.fill_nan(99)



## unnest()
df3.explode('numbers')

## slice
df.slice(1,2)


## select, filter, mutate/with_columns,
(df
  .select(pl.exclude(['d' ]))
  .filter(pl.col("c").is_between(datetime(2022, 12, 2),datetime(2022, 12, 8)))
  .with_columns([
    pl.col('b').sum().alias('b_sum'),
    (pl.col('b') + 42).alias('b+42')
    ]))
    
df.
## group_by
(df2
  .groupby("y", maintain_order=True).count())
(df2
  .groupby("y", maintain_order=True).agg([
    pl.col("x").count().alias("count"),
    pl.col("x").sum().alias("sum")
    ]))

## Combining operations
(df
  .with_column((pl.col("a") * pl.col("b")).alias("a * b"))
  .select([pl.all().exclude(['c', 'd'])]))
