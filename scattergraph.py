import pandas as pd
import plotly.express as px
df = pd.read_csv("data2.csv")
fig = px.bar(df, x = "Population", y = "Per capita", size ="Percentage", color = "Country", size_max = 60 , title = "ScatterGraph Of Various Countries Based On Their Income")
fig.show()
