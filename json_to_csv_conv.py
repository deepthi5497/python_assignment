import json
from pandas.io.json import json_normalize
import csv

def flatten_json(json_data):
    csv_out = {}

    def flatten(data, name=''):
        if type(data) is dict:
            for a in data:
                flatten(data[a], name + a + '_')
                #print(name + a + '_')
        elif type(data) is list:
            i = 0
            for a in data:
                flatten(a, name + str(i) + '_')
                #print(name+str(i)+'_')
                i += 1
        else:
            csv_out[name[:-1]] = data
            print(csv_out)
    flatten(json_data)
    return csv_out

json_data = {"table1": {"tablename":"emp_table","format":"csv","options":["DN","GFF"]},"table2": {"tablename":"dep_table","format":"csv","options":["DNN","HHGFF"]}}
flat_json = flatten_json(json_data)
print(flat_json)
dict_list = []
dict_value_list = []
for k,v in flat_json.items():
    dict_list.append(k)
    dict_value_list.append(v)
print(dict_list)
print(dict_value_list)



