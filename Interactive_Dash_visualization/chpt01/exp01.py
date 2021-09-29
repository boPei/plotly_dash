import matplotlib.pyplot as plt
from plotly.tools import mpl_to_plotly


if __name__ =='__main__':

    mpl_fig,ax=plt.subplots()
    ax.scatter(x=[1,2,3],y=[23,12,34])
    plotly_fig=mpl_to_plotly(mpl_fig)
    plotly_fig

