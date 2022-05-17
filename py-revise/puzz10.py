'''
Parse access logs and find out all the uri's and consolidate them based on timestamp. If on a same timestamp, there are duplicate URI's, then we need to get the count of uris.
for ex: ['timestamp1' :{'uri1:2', uri2:1, uri3: 5}, 'timestampN :{'uri1:2', uri2:1, uri3: 5}]
'''

access_logs = [
    '2019-01-01T00:00:01, 12.21.1.101, GET, /assets/js/loader.js, 102, 0',
    '2019-01-01T00:00:02, 12.21.2.102, GET, /assets/img/hero_100.jpg, 157121, 0',
    '2019-01-01T01:00:01, 12.21.1.102, GET, /assets/js/loader.js, 102, 1',
    '2019-01-01T01:00:01, 12.21.1.102, GET, /assets/js/loader.js, 102, 1',
    '2019-01-01T01:00:01, 12.21.1.102, GET, /assets/js/loader.js, 102, 1',
    '2019-01-01T01:00:01, 12.21.1.102, GET, /assets/js/loader.js, 102, 1',
    '2019-01-01T00:00:01, 12.21.1.101, GET, /assets/js/loader.js, 102, 0',
    '2019-01-01T00:00:02, 12.21.2.102, GET, /assets/img/hero_100.jpg, 157121, 0',
    '2019-01-01T01:00:01, 12.21.1.102, GET, /assets/js/loader.js, 102, 1'
    
]

'''
Solution:
Split logs line and get timestamp and uri.
create a set of dictionary  with key as timestamp and value as uri and its count.
'''
outer_dict,tmp_dict = {},{}

for line in access_logs:
    ts = line.split(",")[0]
    #print(ts)
    uri = line.split(",")[3]
    if ts in outer_dict:
        #print(f'timestamp {ts} already exist in {outer_dict}')
        tmp_dict = outer_dict[ts]
        #print(f'inner dict of {ts} is {tmp_dict}')
        if uri in tmp_dict:
            tmp_dict[uri] +=1
        else:
            tmp_dict[uri] = 1
        outer_dict[ts] = tmp_dict
    else:
        #Adding timestamp
        outer_dict[ts] = {uri:1}

print(f'Final dictonary is {outer_dict}')