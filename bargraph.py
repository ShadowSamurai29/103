import pandas as pd
import plotly.express as px
df = pd.read_csv("data2.csv")
fig = px.bar(df, x = "Country", y = "InternetUsers", title = "BarGraph Of Various Countries Based On Their Income")
fig.show()
