import plotly.plotly as py
import cufflinks as cf
import pandas as pd
import numpy as np
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.mydb.newSubset
video_record1 = {}


cf.set_config_file(offline=False, world_readable=True, theme='ggplot')
results = db.find()
a=[]
for i in results:
  a.append([i['Date'],i['averageRating']])
#for record in results:
df = pd.DataFrame(a,columns=['Date' ,'averageRating'])
df.iplot(kind='bar', barmode='stack', filename='cufflinks/IphoneMain')

