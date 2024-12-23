<!--  cSpell:disable -->
# Ansible Role: Podman Management

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview
Ansible role for Podman installation, configuration, and lifecycle management across Linux distributions.

## Features
  - Install, uninstall, update, and verify Podman
  - Cross-platform support (Fedora 41, Debian 12.8)

## Requirements
- Ansible 2.18+
- Python 3.11

  
## Quick Start

### Clone Repository

```
git clone https://github.com/pycodebe/podman-ansible-role.git
conda env create -f environment.yml
conda activate ansible-role-podman
```

```
# .env

export LOCAL_VENV_BIN=~/miniconda3/envs/ansible-role-podman/bin/
export PYTHON_INTERPRETER=$LOCAL_VENV_BIN/python3.11
export ANSIBLE_PLAYBOOK_BIN=$LOCAL_VENV_BIN/ansible-playbook
```

```
# inventory.cfg

[all]
localhost ansible_connection=local
```

```
# playbook.yml

---
- name: Run ansible role podman
  hosts: all
  gather_facts: true
  roles:
    - role: ansible_role_podman
```

## Usage

This role supports three main actions: **install**, **uninstall**, and **update**.

1. **Install Podman**:

```
source .env
$ANSIBLE_PLAYBOOK_BIN -i inventory.cfg playbook.yml -e "podman_action=install"
```

2. **Uninstall Podman**:

```
source .env
$ANSIBLE_PLAYBOOK_BIN -i inventory.cfg playbook.yml -e "podman_action=uninstall"
```

3. **Update Podman**:

```
source .env
$ANSIBLE_PLAYBOOK_BIN -i inventory.cfg playbook.yml -e "podman_action=update"
```

## Testing


### Run Molecule tests

```
molecule test -s install

molecule test -s uninstall
```

## Dependencies

- None

## License

MIT