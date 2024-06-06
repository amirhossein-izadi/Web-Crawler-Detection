# Web Crawler Detection
This is final project of [Rahnema College](https://rahnemacollege.com/courses/machine_learning_fundamental) Machine Leaning Online bootcamp, An Anomaly detection task for given http logs of [Sanjagh Website](https://sanjagh.pro).


## Project Description

### Introduction
The task is focused on detecting anomalies within datasets, particularly in the context of cybersecurity, to identify intrusions through log analysis.
Anomalies are critical in various domains like banking, cybersecurity, and system administration. 
Traditional log anomaly detection methods, which rely on manual inspection, keyword searches, and regular expressions, are inefficient due to the vast amount of data and evolving attack techniques.
Consequently, modern anomaly detection mechanisms, especially machine learning methods, have been proposed to enhance detection efficiency.

## Dataset
The dataset has been obtained from the Sanjagh server logs. Although it cannot be publicly released, a tiny sample of it can be found [`here`](https://github.com/amirhossein-izadi/Web-Crawler-Detection/blob/master/Datasets) (in <mark>server_HTTP_logs.log</mark> and <mark>log_sample.csv</mark>.
In case you are interested in the complete dataset, you can use any other nginx log servers available in the world-wide internet and extract it and save it into csv file via [`extractor.py`](https://github.com/amirhossein-izadi/Web-Crawler-Detection/blob/master/Utils)

This is server log format
```
IP [Timestamp] [HttpMethod UrlPath] StatusCode ResponseLength [[UserAgent]] ResponseTime
```
and this is a generated sample
```
42.236.10.125 [2020-12-19T15:23:10.0+0100] [GET / http://baidu.com/] 200 10479 [["Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; EML-AL00 Build/HUAWEIEML-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108]] 32
```
