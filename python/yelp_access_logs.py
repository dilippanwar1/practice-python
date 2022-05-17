
access_logs = [
    '2019-01-01T00:00:01, 12.21.1.101, GET, /assets/js/loader.js, 102, 0',
    '2019-01-01T00:00:02, 12.21.2.102, GET, /assets/img/hero_100.jpg, 157121, 0',
    '2019-01-01T01:00:01, 12.21.1.102, GET, /assets/js/loader.js, 102, 1',
    '2019-01-01T01:00:01, 12.21.1.102, GET, /assets/js/loader.js, 102, 1'
]

def get_report(final_dict):
    #print("Asset, Count\n")
    for k,v in final_dict.items():
        print(k,v)

def update_uri_key_count(uri_key, uri_dict):
    if uri_key in uri_dict:
        #print('Key is already present')
        uri_dict[uri_key]+=1
    else:
        #print('Key does not exist')
        uri_dict[uri_key] = 1
    return uri_dict

def rough_update_uri_key_count(uri_key, uri_dict):
    if uri_key in uri_dict:
        #print('Key is already present')
        uri_dict[uri_key]+=1
    else:
        #print('Key does not exist')
        uri_dict[uri_key] = 1
    return uri_dict

def display_access_report(access_logs):
    final_dict = {}
    for log_line in access_logs:
        uri_dict = {}
        uri_key = log_line.split(',')[3]
        uri_timestamp = log_line.split(':')[0]
        #print(uri_timestamp + " and " + uri_key)
        if uri_timestamp in final_dict:
            tmp_dict = final_dict[uri_timestamp]
            if uri_key in tmp_dict:
                #print("URI already exist in internal dict" +uri_key)
                tmp_dict[uri_key]+=1
                #print("tmp dict is" +str(tmp_dict))
                #final_dict.update(tmp_dict)\
                final_dict[uri_timestamp].update(tmp_dict)
                #final_dict[uri_timestamp] = tmp_dict
                #print("final dict is" +str(final_dict))
            else:
                #print("URI does not exist in internal dict" +uri_key)
                tmp_dict[uri_key] = 1
        else:
            final_dict[uri_timestamp] = {uri_key:1}
        

        #final_dict.update(uri_timestamp)
        
        
    get_report(final_dict)
    #print(final_dict)
    

display_access_report(access_logs)