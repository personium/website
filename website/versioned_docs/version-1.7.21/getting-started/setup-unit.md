---
id: version-1.7.21-setup-unit
title: Setup Personium Unit
sidebar_label: Setup Personium Unit
original_id: setup-unit
---

## Introduction

This section describes the construction of Personium Unit. As an introduction, we will build an All-in-one Personium Unit with an Ansible Playbook that allows all the roles of one server on IaaS.

If you want to build with other configurations, please refer to [Server Software Operator's Guide](../server-operator/README.md).

## Precautions

Personium Unit assumes that HTTPS access is performed in different subdomains depending on the data subject such as `https://alice.personium.example` and `https://bob.personium.example`, so the followings are required.

-DNS record setting with a wildcard domain name such as `*.personium.example` for the IP address accessing the web server
-Get and set SSL certificate corresponding to wildcard domain name such as `*.personium.example`

To simplify the above, it is recommended to build the Personium Unit using public IaaS and DNS service rather than building on a local network. This section introduces the steps based on public IaaS and DNS service.

## Unit construction

### Create VM

Create a VM with public IaaS. The parameters suggested below has been confirmed recently. (As of June 2020)

| Item | Value |
|----|----|
|IaaS|Microsoft Azure Virtual Machines|
|OS|CentOS 7|
| Size | Standard B2ms (2 vcpu number, 8 GiB memory) |
|OS Disk |30 GiB|
| Public IP address | Yes |

> Personium itself works on OSs other than CentOS7, but since the Ansible Playbook that we tested is based on CentOS7, please use CentOS7 series to avoid any configuration trouble.

### Security group/firewall settings

To create and access the Personium Unit, set the security group/firewall to allow access to the following ports for the created VM.

| Direction | Port | Source | Destination | Purpose |
|-----------|------|--------|-------------|---------|
| Inbound | 443 | any | any |Allow access to the Personium API through HTTPS |
| Inbound | 22 | your work machine | any | Allow access to the created VMs through SSH |
| Outbound | 443 | any | any | External repositories access using HTTPS |
| Outbound | 80 | any | any | External repositories access using HTTP |

### Personium installation using Ansible

Follow the steps in the document below.

[Personium Ansible Playbook 1-server](https://github.com/personium/ansible/tree/develop/1-server_unit)

If successful, the Personium Unit will be built.

### Confirm access to Personium Unit

Access `https://{Personium Unit domain name}/` with a browser. A response in the following format is displayed.

```json
{"unit":{"path_based_cellurl_enabled":false,"url":"https:\/\/{Personium Unit domain name}\/"}}
```

### Access information for Personium Unit management

When built with Ansible Playbook, a Unit management account for creating Cells will be created. For details on the Unit management account, refer to the following document.

[Personium Unit management account](../server-operator/Confirm_environment_settings.md#personium-unit-management-account)
