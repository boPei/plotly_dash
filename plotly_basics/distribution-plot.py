import numpy as np
import plotly.figure_factory as ff
import plotly.offline as pyo

x1=np.random.randn(1000)-2
x2=np.random.randn(1000)
x3=np.random.randn(1000)+2
x4=np.random.randn(1000)+4


dist_data=[x1,x2,x3,x4]
dist_labels=['X1','X2','X3','X4']

fig=ff.create_distplot(dist_data,dist_labels,bin_size=[.1,.2,.3,.4])
pyo.plot(fig)