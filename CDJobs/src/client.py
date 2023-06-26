import requests

print(requests.post("http://127.0.0.1:8000/deploy/images?deploy_server_ip=172.27.40.36&deploy_dir=True&image_name=prod-ce").json())
