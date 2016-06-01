# Please change ownership for all issues in bugs.json to 'qa5'. Save result to bugs_new.json. Use json loads and dumps methods.
import json
from pprint import pprint
data_file2=open('bugs.json')
data2=json.load(data_file2)
for i in data2:
     i['Owner']='qa5'
     # print i
     with open('bugs_new.json','w') as data_file:
         data_file.write(json.dumps(i))
         data_file.close()