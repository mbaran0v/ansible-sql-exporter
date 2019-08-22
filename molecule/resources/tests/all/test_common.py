
debian_os = ['debian', 'ubuntu']
rhel_os = ['redhat', 'centos']
version = '0.2.0'
root_dir = '/opt/sql_exporter'


def test_distribution(host):
    assert host.system_info.distribution.lower() in debian_os + rhel_os


def test_install_dir(host):
    f = host.file(root_dir)

    assert f.exists
    assert f.is_directory


def test_release_dir(host):
    f = host.file(root_dir + '/releases/' + version)

    assert f.exists
    assert f.is_directory


def test_release_symlink_dir(host):
    f = host.file(root_dir + '/current')

    assert f.exists
    assert f.is_symlink
    assert f.linked_to == root_dir + '/releases/' + version


def test_service(host):
    s = host.service('sql_exporter')

    assert s.is_enabled
    assert s.is_running


def test_user(host):
    u = host.user('sql-exp')

    assert u.exists
    assert u.group == 'sql-exp'
    assert u.shell == '/usr/sbin/nologin'


def test_config(host):
    f = host.file(root_dir + '/releases/' + version + '/sql_exporter.yml')

    assert f.exists
    assert oct(f.mode) == '0o600'
