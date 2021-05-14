# Kafka Processor Environment

The Kafka processor is a project to build a streaming data processing, and use a scalable environment using Kubernetes. 

The operating system used for create this environment is an ***Ubuntu 20.04.2 LTS***.

##### If you don't know your operating system version, it's not a problem, use one of the commands below to checkout this:

### Ubuntu
```
# lsb_release -a
```

### Debian
```
# lsb_release -d
```

### Mac OS
```
# sw_vers
```

To build a streaming data processing, we use a Kafka on Kubernetes using minikube to test environment.

# Setup Environment

## Installing VirtualBox

```
sudo apt-get update

sudo apt-get install virtualbox

```


## Installing Kubernetes and Minikube

### Kubectl

```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

curl -LO "https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"

echo "$(<kubectl.sha256) kubectl" | sha256sum --check

sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

kubectl version --client
```

### Minikube

```
curl -Lo minikube https://github.com/kubernetes/minikube/releases/download/v0.28.0/minikube-linux-amd64

chmod +x minikube && mv minikube /usr/local/bin/
```

#### Solving problems:

```
minikube stop
minikube delete
minikube start
```

To build kafka on test environment, we use the Helm to manage Kubernetes applications, and provide the Kafka as a pod. 

## Installing Helm from Apt (Debian/Ubuntu)
```
curl https://baltocdn.com/helm/signing.asc | sudo apt-key add -
sudo apt-get install apt-transport-https --yes
echo "deb https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt-get update
sudo apt-get install helm
```

