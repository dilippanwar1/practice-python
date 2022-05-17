import json
with open('logs/nginx_json_logs.json') as json_file:
    log = json.load(json_file)
    print(json.dumps(log, indent=2))