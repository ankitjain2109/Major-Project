import plotly.plotly as py
import plotly.graph_objs as go
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.mydb.newSubset
db2 = client.mydb.final
result=db.find()
result2=db2.find()
x={}
y=[]
z=[]
for i in result:
    y.append(i['Date'])
    z.append(i['averageRating'])
	#x.update({i['Date']:i['averageRating']})
	#x.append(i['PublishedAt'])
	#y.append(i['popularity'])
#sorted(x.items())
#y=x.keys()
#z=x.values()
data = [
    go.Scatter(
       x=y,
       y=z
    )
]
plot_url = py.plot(data, filename='date-axes')

for i in result2:
    data=[
        go.Scatter(
            x=i['Date'],
            y=i['Weight']
            )
        ]
plot_url1=py.plot(data,filename='date2')
