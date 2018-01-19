#https://plot.ly/python/line-charts/
import plotly.plotly as py
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go

price = [5, 5.5, 5.5, 4, 3, 3.2, 3.5, 4.5, 6]

x_axis = list(range(0, len(price)))
y_axis = price
print(x_axis)  

trace = go.Scatter(
    x = x_axis,
    y = y_axis,
    name = "Positive"
)


trace2 = go.Scatter(
    x = x_axis,
    y = y_axis[::-1],
    name = "Negative"
)

data = [trace, trace2]


plot(data, filename="test")