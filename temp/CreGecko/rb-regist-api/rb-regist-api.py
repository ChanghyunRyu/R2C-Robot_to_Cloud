import json, yaml
from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics
from os import path
from kubernetes import client, config

app = Flask(__name__)
metrics = PrometheusMetrics(app)
config.load_incluster_config()


@app.route('/regist', methods=['POST'])
def robot_registration():
    response = {'success': False}

    # parameters = {'name': '<robot name>'}, request.post
    paramaters = json.loads(request.get_data())
    name = paramaters['name']
    response['success'] = True

    # Deployment create, rb_name = name
    # explore.yaml
    with open(path.join(path.dirname(__file__), "rb-function/explore.yaml")) as file:
        dep = yaml.safe_load(file)
        # paramater change
        dep['metadata']['name'] = 'ros-explore-lite-{}'.format(name)
        dep['spec']['template']['spec']['containers'][0]['env'][1]['value'] = '{}'.format(name)
        k8s_apps_v1 = client.AppsV1Api()
        resp = k8s_apps_v1.create_namespaced_deployment(body=dep, namespace="default")
        print("Deployment created. status='%s'" % resp.metadata.name)

    # move.yaml
    with open(path.join(path.dirname(__file__), "rb-function/move.yaml")) as file:
        dep = yaml.safe_load(file)
        # paramater change
        dep['metadata']['name'] = 'ros-move-base-{}'.format(name)
        dep['spec']['template']['spec']['containers'][0]['env'][1]['value'] = '{}'.format(name)
        k8s_apps_v1 = client.AppsV1Api()
        resp = k8s_apps_v1.create_namespaced_deployment(body=dep, namespace="default")
        print("Deployment created. status='%s'" % resp.metadata.name)

    # slamgmapping.yaml
    with open(path.join(path.dirname(__file__), "rb-function/slamgmapping.yaml")) as file:
        dep = yaml.safe_load(file)
        # paramater change
        dep['metadata']['name'] = 'ros-slam-gmapping-{}'.format(name)
        dep['spec']['template']['spec']['containers'][0]['env'][1]['value'] = '{}'.format(name)
        k8s_apps_v1 = client.AppsV1Api()
        resp = k8s_apps_v1.create_namespaced_deployment(body=dep, namespace="default")

        print("Deployment created. status='%s'" % resp.metadata.name)

    # statepublisher.yaml
    with open(path.join(path.dirname(__file__), "rb-function/statepublisher.yaml")) as file:
        dep = yaml.safe_load(file)
        # paramater change
        dep['metadata']['name'] = 'ros-slam-gmapping-{}'.format(name)
        dep['spec']['template']['spec']['containers'][0]['env'][1]['value'] = '{}'.format(name)
        k8s_apps_v1 = client.AppsV1Api()
        resp = k8s_apps_v1.create_namespaced_deployment(body=dep, namespace="default")
        print("Deployment created. status='%s'" % resp.metadata.name)

    # statictransformpublisher.yaml
    with open(path.join(path.dirname(__file__), "rb-function/statictransformpublisher.yaml")) as file:
        dep = yaml.safe_load(file)
        # paramater change
        dep['metadata']['name'] = 'ros-static-transform-publisher-{}'.format(name)
        dep['spec']['template']['spec']['containers'][0]['env'][1]['value'] = '{}'.format(name)
        k8s_apps_v1 = client.AppsV1Api()
        resp = k8s_apps_v1.create_namespaced_deployment(body=dep, namespace="default")
        print("Deployment created. status='%s'" % resp.metadata.name)
    return response


@app.route('/')
def get_check():
    return "checking Running Server"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8081')

