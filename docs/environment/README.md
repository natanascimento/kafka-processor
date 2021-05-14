## Kafka Processor Environment

To build a streaming data processing, we use a Kafka on Kubernetes.

For this, we use the Helm to manage Kubernetes applications, and provide the Kafka as a pod. 

The operating system used for create this environment is an ***Ubuntu 20.04.2 LTS***

##### If you don't know your operating system version, it's not a problem, use one of the commands below to checkout this:

### Ubuntu
```
$ lsb_release -a
```

### Debian
```
$ lsb_release -d
```

### Windows
```
- [Windows] key + [R] - To open "Run" dialog box.
- Write winver and click on [OK].
```

### Mac OS
```
$ sw_vers
```