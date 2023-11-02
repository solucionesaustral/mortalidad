# -*- coding: utf-8 -*-
"""
Created on Mon May 29 09:09:59 2023

@author: mauricio
"""

import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

google_drive_link = "https://drive.google.com/file/d/1uOPzQO_hoHS_Dls52sST5DxGCu2Ko3ac/view?usp=sharing"
google_drive_link ='https://drive.google.com/uc?id=' + google_drive_link.split('/')[-2]
df = pd.read_csv(google_drive_link, delimiter = ';')

  
app = Dash(__name__)
server = app.server

fig = px.line(df, x='fecha', y= "mortalidad", title= "Gráfico de Mortalidad", template = "plotly_dark")

app.layout=html.Div([     
            html.H1(children='Mortalidades'),
            html.Div(children='''
                Centro de cultivo
            '''),
            dcc.Graph(id='ejemplo', 
                      figure=fig)
])                   
                    
if __name__ == "__main__":
    app.run_server(debug=False)

