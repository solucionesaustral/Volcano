# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UKkuUOpv3N1wG5Xnw6_FgCAIJxextjox
"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install Dash



from dash import Dash, dcc, html, Input, Output

import pandas as pd
import plotly.express as px

mydataset = "https://raw.githubusercontent.com/plotly/datasets/master/volcano_db.csv"

df = pd.read_csv(mydataset, encoding="latin")

df.head()

app = Dash(__name__)
server = app.server
app.layout = html.Div([
    html.Header('My Volcano App por mr'),
    dcc.Dropdown(id="mydropdown",
                 options=df["Type"].unique(),
                 value="Stratovolcano"),
    dcc.Graph(id = "my_scatter_geo")
])

@app.callback(Output("my_scatter_geo", "figure"),
              Input("mydropdown", "value"))
def sync_input(volcano_selection):
  fig = px.scatter_geo(df.loc[df["Type"] == volcano_selection],
                       lat="Latitude",
                       Lon="Longitude",
                       size="Elev",
                       hover_name="Volcano Name")
  return fig



if __name__ == "__main__":
  app.run_server(debug=False)
