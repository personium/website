---
id: unit-setup
title: Unit Setup
sidebar_label: Unit Setup
---

## Introduction

You can choose various system structure like followings.

- Any Machine(s)
  - all-in-one
  - 3-tier
- Local VM
- Local Containers

In this section, we introduced one simple way that is all-in-one on IaaS VM with Ansible Playbook.
If you want to choose other way, please see [Server Software Operator's Guide](../server-operator/README.md).

## Notes

Personium requires followings.

- Wild card subdomain DNS settings so that users can access Personium url like `user1.personium.example` or `user2.personium.example`.
- SSL Server certificate settings to access by HTTPS.

To set up above easily, we recommend public IaaS server rather than local server.
On public IaaS, you can use DNS service and server certificate service.

## Setup

### Create VM

TODO

### Set DNS

TODO

### Create server certificate

TODO

### Install Personium with Ansible

TODO
