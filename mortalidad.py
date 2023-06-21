# -*- coding: utf-8 -*-
"""
Created on Mon May 29 09:09:59 2023

@author: mauricio
"""

import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

df = pd.read_csv('http://solucionesaustral.cl/Llaguepe2.csv', delimiter = ';')
  
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
