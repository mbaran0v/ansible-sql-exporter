# Ansible role: Prometheus SQL Exporter

[![Build Status](https://travis-ci.org/mbaran0v/ansible-role-sql-exporter.svg?branch=master)](https://travis-ci.org/mbaran0v/ansible-role-sql-exporter)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![GitHub tag](https://img.shields.io/github/tag/mbaran0v/ansible-role-sql-exporter.svg)](https://github.com/mbaran0v/ansible-role-sql-exporter/tags/)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

Ansible role for [Prometheus SQL Exporter](https://github.com/justwatchcom/sql_exporter). Currently this works on Debian and RedHat based linux systems. Tested platforms are:

* Ubuntu 16.04
* CentOS 7

Requirements
------------

None

Role Variables
--------------

The variables that can be passed to this role and a brief description about them are as follows. (For all variables, take a look at defaults/main.yml)

```yaml
# sql exporter version
sql_exporter_version: "0.2.0"

# see https://github.com/justwatchcom/sql_exporter/blob/master/config.yml.dist
sql_exporter_config:
  jobs:
    - name: "example"
      interval: '5m'
      connections:
        - 'postgres://postgres@localhost/postgres?sslmode=disable'
      queries:
        - name: "running_queries"
          help: "Number of running queries"
          labels:
            - "datname"
            - "usename"
          values:
            - "count"
          query: |
            SELECT datname::text, usename::text, COUNT(*)::float AS count
            FROM pg_stat_activity GROUP BY datname, usename;
```

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: sql-exporter
  roles:
      - role: mbaran0v.sql-exporter
```

License
-------

MIT / BSD

Author Information
------------------

This role was created in 2018 by [Maxim Baranov](https://github.com/mbaran0v).
