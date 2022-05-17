def get_file_chunk(fh, chunk_size=1024):
    data = fh.read(chunk_size)
    while True:
        if not data:
            break
        yield data

def parse_chunk(piece):
    print("I am processng chunka::::  " + piece)

with open('logs/nginx_json_logs.txt') as fh:
   for piece in get_file_chunk(fh):
     parse_chunk(piece) 