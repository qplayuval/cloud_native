import requests

print(requests.post("http://127.0.0.1:6666/deploy/images?git_ip=172.27.40.36&url_path=ansible/collection/carrier-ethernet&deploy_name=prod-ce.yaml").json())
