import json
import pandas as pd
from datetime import datetime
from matplotlib.pyplot import MultipleLocator
with open('../data/ding.json', 'r') as f:
    js_dic = json.load(f)
data =  js_dic["data"]
application = data[0]["data"]
ios = data[-1]["data"]
import matplotlib.pyplot as plt

dates = []
application_data = []
ios_data = []
for i  in range(len(application)):
    dates.append(list(application[i].keys())[0])
    if list(application[i].values())[0] !='-':
        application_data.append(int(list(application[i].values())[0]))
    else:
        application_data.append(int(list(application[i-1].values())[0]))
    if list(ios[i].values())[0] !='-':
        ios_data.append(int(list(ios[i].values())[0]))
    else:
        ios_data.append(int(list(ios[i-1].values())[0]))



print(max(ios_data))

dates =  [datetime.strptime(d,'%Y-%m-%d').date() for d in dates]
plt.plot(dates,application_data,label="ranking in all android and ios free applications")
plt.plot(dates,ios_data,label="ranking in all ios free applications")
y_major_locator=MultipleLocator(50)
ax=plt.gca()
ax.yaxis.set_major_locator(y_major_locator)

plt.ylim([0, 300])
plt.title(u'Application store rank of dingtalk')
plt.xlabel("date")
plt.ylabel("application rank")

plt.legend()
plt.savefig("dingtalk.png")
plt.show()
