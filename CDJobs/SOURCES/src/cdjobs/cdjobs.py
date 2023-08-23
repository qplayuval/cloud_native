import tempfile
import requests
from fastapi import FastAPI
from kubernetes import client,config,utils

app = FastAPI()

def download_kubernetes_deploy(tmpdir,
        deploy_name,
        git_ip,
        url_path):
    response = requests.get(f"http:/{git_ip}/{url_path}/{deploy_name}")

    with open(f"{tmpdir}/deploy_name") as deploy_file:
        deploy_file.write(response.context)

def deploy_kubernetes_job(tmpdir, deploy_name):
    config.load_kube_config()
    k8s_client = client.ApiClient()
    yaml_dir = tmpdir
    utils.create_from_directory(k8s_client, yaml_dir,verbose=True)

@app.post("/deploy/images")
def deploy(git_ip: str,
           url_path: str,
           deploy_name: str = "prod-ce"):

    with tempfile.TemporaryDirectory() as tmpdir:
        download_kubernetes_deploy(tmpdir,
            deploy_name,
            git_ip,
            url_path)
        deploy_kubernetes_job(tmpdir, deploy_name)
    return { "ce": "deployed", "gitIp": git_ip, "imageName": deploy_name, "deployDir": url_path }
