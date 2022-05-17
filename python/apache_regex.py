import re
from typing import Counter

with open('logs/apache_logs.txt') as file:
    f = file.read()
    get_ip_list = re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',f)
    get_ips_with_count = Counter(get_ip_list)
    #print(get_ip_list)
    ip_keys_map = dict(get_ips_with_count)
    #print(ip_keys_map)
    ip_dict = {}
    for ip in get_ip_list:
        if ip in ip_dict:
            #get value of that key and increment by 1
            ip_dict[ip]+= 1
        else:
            #add key to dict and with value=1
            ip_dict[ip] = 1

#print(ip_dict)
        abc = {"hi":"hello", "dsf": "kjafkj"
        
        }
    for key, value in enumerate(abc):
        print(key,value)
    
    


