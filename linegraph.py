import pandas as pd
import plotly.express as px
df = pd.read_csv("data.csv")
fig = px.line(df, x = "Country", y = "Per capita income", color = "Country", title = "LineGraph Of Various Countries Based On Their Income")
fig.show()



