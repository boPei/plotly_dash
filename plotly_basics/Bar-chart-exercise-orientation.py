import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

df=pd.read_csv('mocksurvey.csv',index_col=0)
print(df)

trace=[go.Bar(y=df.index,
              x=df[response],
              orientation='h',
              name=response) for response in df.columns]
layout=go.Layout(title='Mock Survey Results',
                 barmode='stack')

fig=go.Figure(data=trace,layout=layout)

pyo.plot(fig)