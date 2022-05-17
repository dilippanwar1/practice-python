import re
from typing import Counter

with open('logs/nginx_logs.txt') as file:
    log = file.read()
    #print(log)
    http_code_list = re.findall('(?:304|200|404)', log)
    print(type(http_code_list))
    resp_code_count = Counter(http_code_list)


    #print(resp_code_count)
    for k,v in resp_code_count.items():
        print("Count of HTTP error code " + k + " is " +str(v))

