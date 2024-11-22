import pandas as pd # type: ignore
import numpy as np # type: ignore

df = pd.read_csv('articles.csv')

df = df.sort_values(['total_events'], ascending=[False])

output = df[["url", "title", "text", "lang", "total_events"]].head(20)