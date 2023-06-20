# -*- coding: utf-8 -*-
"""
Created on Mon May 29 09:09:59 2023

@author: mauricio
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

df = []
df = pd.read_csv('c:\Python2\Llaguepe2.csv', delimiter = ';')
fr = pd.DataFrame(df)
 
fr.head()

   fig = px.line(fr, x='fecha', y= "mortalidad", title= "Gráfico de Mortalidad", template = "plotly_dark"),
  fig.show()  

app=dash.Dash()
app.layout=html.Div([
     
            html.H1(children='Mortalidades'),
            html.Div(children='''
                Centro de cultivo
            '''),
            dcc.Graph(figure={
                "fr": [{
                    "x": fr["fecha"],
                    "y": fr["mortalidad"],
                    "type": "lines",
                    },
                    ],
                "layout":{"title": "Mortalidad del centro en meses"},
                },         
               
            ),  
   
  

]) 
if __name__ == "__main__":
    app.run_server(debug=False)

x=df['mortalidad']
x
x.head()
