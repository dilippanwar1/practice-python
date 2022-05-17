import json
placeholder = '__STRATOSPHERE_SVC_NAME__'
#json_data = {}
servicname = ''
with open('logs/json_tmpl.json') as jsonfile:    
    json_data = json.load(jsonfile)
    
    print(type(json_data))
    servicename = json_data['params']['serviceName']
    print("Servicename is: " +servicename)
    with open('logs/newjson.json', 'r+') as jsonf:

        #jh = json.load(jsonf)
        #jh.replace(placeholder, servicename)
        
       
        print(jsonf)


#jsonfile.close()
#with open('logs/newjson.json', 'w') as jsonf:
#    json.dump(json_data, jsonf, indent=4)
#jsonf.close()

#'''Read service name and update it in another json file'''





