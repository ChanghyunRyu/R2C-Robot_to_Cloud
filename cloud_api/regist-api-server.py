import json, yaml
from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics
from os import path
import time
from kubernetes import client, config

config.load_kube_config()
app = Flask(__name__)
metrics = PrometheusMetrics(app)


@app.route('/regist', methods=['POST'])
def robot_registration():
    response = {'success': False}

    # parameters = {'name': '<robot name>'}, request.post
    paramaters = json.loads(request.get_data())
    name = paramaters['name']
    response['success'] = True
    k8s_apps_v1 = client.AppsV1Api()

    # statepublisher.yaml
    with open(path.join(path.dirname(__file__), "rb-function/statepublisher.yaml")) as file:
        dep = yaml.safe_load(file)
        # paramater change
        dep['spec']['template']['spec']['containers'][0]['env'][1]['value'] ='{}'.format(name)
        dep['metadata']['name'] = 'ros-state-publisher-{}'.format(name.replace('_', '-'))
        resp = k8s_apps_v1.create_namespaced_deployment(body=dep, namespace="default")
        print("Deployment created. status='%s'" % resp.metadata.name)

    time.sleep(5)

    # Deployment create, rb_name = name
    # slamgmapping.yaml
    with open(path.join(path.dirname(__file__), "rb-function/slamgmapping.yaml")) as file:
        dep3 = yaml.safe_load(file)
        # paramater change
        dep3['spec']['template']['spec']['containers'][0]['env'][1]['value'] ='{}'.format(name)
        dep3['metadata']['name'] = 'ros-slam-gmapping-{}'.format(name.replace('_', '-'))
        k8s_apps_v1 = client.AppsV1Api()
        resp = k8s_apps_v1.create_namespaced_deployment(body=dep3, namespace="default")
        print("Deployment created. status='%s'" % resp.metadata.name)

    time.sleep(5)

    # mapmerge.yaml
    try:
        k8s_apps_v1.delete_namespaced_deployment(name='ros-map-merge', namespace='default')
    except:
        print('map merge is not existe')
    with open(path.join(path.dirname(__file__), "rb-function/mapmerge.yaml")) as file:
        dep6 = yaml.safe_load(file)
        # paramater change
        resp = k8s_apps_v1.create_namespaced_deployment(body=dep6, namespace="default")
        print("Deployment created. status='%s'" % resp.metadata.name)
    return response


@app.route('/')
def get_check():
    return "checking Running Server"


if __name__=='__main__':
    app.run(host='114.70.21.161', port='8082')

