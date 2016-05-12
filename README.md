[![Build Status](https://travis-ci.org/georgepsarakis/django-mesos-example.svg?branch=master)](https://travis-ci.org/georgepsarakis/django-mesos-example)

# Deploying a dockerized Django application on Mesos

This project serves as an example on how a Django application can be deployed on a Mesos cluster using Docker containers.

The main goal is to provide a development environment that can be very similar to modern production architectures.

The project contains:

- Sample Django application using:
  * Django-REST-Framework
  * MySQL
- Ansible playbook that facilitates Vagrant operations.
- Ansible playbook that provisions the VM and deploys the application.

> This is mostly an experimental project. All feedback is appreciated!

## Deployed & Installed Components

- [Mesos](http://mesos.apache.org/)
- [Marathon](https://mesosphere.github.io/marathon/)
- [Zookeeper](https://zookeeper.apache.org/)
- [Mesos-DNS](https://mesosphere.github.io/mesos-dns/)
- [Marathon-LB](https://github.com/mesosphere/marathon-lb)
- [MySQL](https://www.mysql.com/)
- [Nginx](http://nginx.org/)
- [Docker](https://docs.docker.com/)
- [uWSGI](http://uwsgi.readthedocs.io/en/latest/)

## Requirements

Most requirements can be found in the [Travis-CI](https://github.com/georgepsarakis/django-mesos-example/blob/master/.travis.yml) file.

The amount of installed packages is rather large, so using a VM configured by [Vagrant](https://www.vagrantup.com/) is highly recommended.

## Getting Started

### Using Vagrant

```bash
$ ./django-mesos-example 
Valid tasks are: [halt,logs,deploy,destroy,recreate]
```

Default configuration can be found [here](https://github.com/georgepsarakis/django-mesos-example/blob/master/provisioning/roles/vagrant/defaults/main.yml).

When deployment is complete, the following application HTTP interfaces can be reached:

- Mesos http://localhost:5050
- Marathon http://localhost:8080
- Django REST API application http://localhost:7070

#### `deploy`

Start the VM if not already started and proceed with provisioning.

#### `halt`

Stop the VM.

#### `destroy`

Destroy the VM.

#### `logs`

Display the output and error log files using `tail`.

#### `recreate`

Combination of `destroy` & `deploy`.






