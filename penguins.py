# 0. Setup ----------------------------------------------------------------
import polars as pl
import pandas as pd
import numpy as np
from plotnine import *


# 1. Prep data ----------------------------------------------------------------
{
  df = pd.DataFrame({
    'variable': ['gender', 'gender', 'age', 'age', 'age', 'income', 'income', 'income', 'income'],
    'category': ['Female', 'Male', '1-24', '25-54', '55+', 'Lo', 'Lo-Med', 'Med', 'High'],
    'value': [60, 40, 50, 30, 20, 10, 25, 25, 40],
})
df['variable'] = pd.Categorical(df['variable'], categories=['gender', 'age', 'income'])
df['category'] = pd.Categorical(df['category'], categories=df['category'])
df
}

# 2. Plot ----------------------------------------------------------------

(
  ggplot(df, aes(x='variable', y='value', fill='category'))
  + geom_col(stat='identity', position='dodge')
)   

