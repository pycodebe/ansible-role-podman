<!--  cSpell:disable -->
# Ansible Role: Podman Management

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview
This Ansible role manages Podman installation, configuration, and lifecycle across different Linux distributions.

## Features
- Install Podman
- Uninstall Podman
- Update Podman
- Verify Podman installation
- Cross-platform support

## Requirements
- Ansible 2.18+
- Python 3.11
- Supported Operating Systems:
  - Fedora 41
  - Debian 12.8
  
## Installation

### Clone Repository

```
git clone https://github.com/pycodebe/podman-ansible-role.git
```

## Conda Environment Management

### Environment Configuration
The project uses a Conda environment defined in `environment.yml`:

#### Create Environment

```
conda env create -f environment.yml
```

#### Activate Environment

```
conda activate ansible-role-podman
```

#### Verify Environment

```
# Check Python version
python --version

# Verify installed packages
pip list | grep -E "molecule|ansible|podman"
```

## Usage

### Recommended Workflow
1. Clone the repository
2. Create the Conda environment
3. Activate the environment
4. Run tests or execute Ansible playbooks

###  Using the Playbook
This project uses a .env file to manage environment variables. Here's an example of the .env file content:

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

### Running the Playbook

First, source the .env file:

```
source .env
```

Then, use one of the following commands to run the playbook for different actions:

```
# install

$ANSIBLE_PLAYBOOK_BIN -i inventory.cfg playbook.yml -e "podman_action=install"
```

```
# uninstall

$ANSIBLE_PLAYBOOK_BIN -i inventory.cfg playbook.yml -e "podman_action=uninstall"
```

```
# update

$ANSIBLE_PLAYBOOK_BIN -i inventory.cfg playbook.yml -e "podman_action=update"
```

## Tests

### Run Tests

Ensure you're in the ansible-role-podman environment

```
conda activate ansible-role-podman
```

### Run Molecule tests

```
# Run molecule test for the install scenario and the distribution fedora

MOLECULE_CONTEXT=fedora molecule test -s install
```


## Dependencies

- None

## License

MIT