import pandas as pd 
import re

file_path = 'your_log_path.log'
parsed_data = []

counter = 0
with open(file_path, 'r') as file:
    
    # IP [TimeStamp] [Method URL] StatusCode ResponseLength [[UserAgent]] ResponseTime
    pattern = r'(\d+\.\d+\.\d+\.\d+) \[(.*?)\] \[(.*?)\] (\d+) (\d+) \[\[(.*?)\]\] (\d+)'
    for line in file:
     
        match = re.match(pattern, line)
        
        if match:
            ip = match.group(1)
            timestamp = match.group(2)
            request_info = match.group(3)
            http_method, url_path = request_info.split(' ', 1)
            status_code = int(match.group(4))
            response_length = int(match.group(5))
            user_agent = match.group(6)
            response_time = int(match.group(7))
            
            
            parsed_line = {
                'ip': ip,
                'timestamp': timestamp,
                'http_method': http_method,
                'url_path': url_path,
                'status_code': status_code,
                'response_length': response_length,
                'user_agent': user_agent,
                'response_time': response_time
                
            }
            
            parsed_data.append(parsed_line)


            
df = pd.DataFrame(parsed_data)
df.to_csv('../Datasets/log.csv', index=False)
print('done')