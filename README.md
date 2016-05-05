[![Build Status](https://travis-ci.org/georgepsarakis/django-mesos-example.svg?branch=master)](https://travis-ci.org/georgepsarakis/django-mesos-example)

# Deploying a dockerized Django application on Mesos

This project serves as an example on how a Django application can be deployed on a Mesos cluster using Docker containers.

The project contains:

- Sample Django application using Django-REST-Framework. MySQL is used as a backend.
- Ansible playbook that wraps Vagrant operations.
- Ansible playbook that provisions the VM and deploys the application.

> This is still beta-level and experimental. All feedback is appreciated!

## Components

- Mesos
- Marathon
- Zookeeper
- Mesos-DNS
- Marathon-LB (HAproxy)
- MySQL
- Nginx
- Docker

## Requirements

The project was mainly built using Vagrant but is not required.

