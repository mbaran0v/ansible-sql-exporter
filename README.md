# Ansible role: Prometheus SQL Exporter

Ansible role for [Prometheus SQL Exporter](https://github.com/free/sql_exporter). Currently this works on Debian and RedHat based linux systems. Tested platforms are:

* Ubuntu 16.04
* CentOS 7

Requirements
------------

None.

Role Variables
--------------

The variables that can be passed to this role and a brief description about them are as follows. (For all variables, take a look at defaults/main.yml)

```yaml
# kibana version
sql_exporter_version: "0.4"
```

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- hosts: sql-exporter
  roles:
      - { role: mbaran0v.sql-exporter }
```

License
-------

MIT / BSD

Author Information
------------------

This role was created in 2018 by Maxim Baranov.
