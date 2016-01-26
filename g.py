import plotly.plotly as py
import plotly.graph_objs as go
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
#db = client.mydb.newSubset
db2 = client.mydb.final
#result=db.find()
result2=db2.find()
x=[]
y=[]
z={}
for i in result2:
    z.update({i['Date']:i['Weight']})
    #x.append(i['Date'])
    #y.append(i['Weight'])
sorted(z.items())
x=z.keys()
y=z.values()
data=[
        go.Scatter(
            x=x,
            y=y
            )
        ]
plot_url1=py.plot(data,filename='date2')

