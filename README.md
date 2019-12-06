Ansible role for nfs
==================================

Installs nfs packages on the host

[![CircleCI](https://img.shields.io/circleci/build/github/mongodb-ansible-roles/ansible-role-nfs/master?style=flat-square)](https://circleci.com/gh/mongodb-ansible-roles/ansible-role-nfs)

Requirements
------------

None

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| `nfs_user` | User that will be using nfs packages | string | `root` | yes

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-nfs
      vars:
        nfs_user: admin
```

Development
-----------

Testing this role locally requires the CircleCI [Local CLI](https://circleci.com/docs/2.0/local-cli/).

To install the CLI for macOS and Linux, invoke the following command:

    $ curl -fLSs https://circle.ci/cli | DESTDIR=/usr/local/bin bash

After installing the CLI, invoke the following command to run the Molecule tests:

    $ make test

License
-------

[Apache License](LICENSE)
