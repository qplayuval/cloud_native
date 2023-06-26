#import constants.py
from git import Repo
from fastapi import FastAPI
#from kubernetes import client,config,utils

app = FastAPI()

#def clone_git_repo():
#    Repo.clone_from(GIT_URL, LOCAL_PATH)

#def deploy_kubernetes_job():
#    config.load_kube_config()
#    k8s_client = client.ApiClient()
#    yaml_dir = 'examples/yaml_dir/'
#    utils.create_from_directory(k8s_client, yaml_dir,verbose=True)

@app.post("/deploy/images")
def deploy(deploy_server_ip: str, deploy_dir: bool = False, image_name: str = "prod-ce"):
#   clone_git_repo()
#   deploy_kubernetes_job()
    return { "ce": "deployed", "serverIp": deploy_server_ip, "imageName": image_name, "deployDir": deploy_dir }
