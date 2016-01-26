import plotly.plotly as py
from pymongo import MongoClient
import plotly.graph_objs as go
client = MongoClient()
db1 = client.test0.testing10
result=db1.find()
x={}
y=[]
z=[]
for i in result:
	x.update({i['PublishedAt']:i['popularity']})
	#x.append(i['PublishedAt'])
	#y.append(i['popularity'])
sorted(x.items())
y=x.keys()
z=x.values()
data = [
    go.Scatter(
       x=y,
       y=z
    )
]
plot_url = py.plot(data, filename='date-axes', kind='bar',barmode='stack')

cf.set_config_file(offline=False, world_readable=True, theme='ggplot')
#for record in results:
df = pd.DataFrame(z,columns=['P'])
plot_url =df.iplot(kind='bar', barmode='stack', filename='cufflinks/stacked-bar-chart')
