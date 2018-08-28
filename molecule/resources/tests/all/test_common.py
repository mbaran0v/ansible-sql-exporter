
debian_os = ['debian', 'ubuntu']
rhel_os = ['redhat', 'centos']


def test_distribution(host):
    assert host.system_info.distribution.lower() in debian_os + rhel_os


def test_config(host):
    f = host.file('/opt/sql_exporter/current/sql_exporter.yml')

    assert f.exists


def test_socket(host):
    s = host.socket('tcp://:::9237')
    print(host.socket.get_listening_sockets())

    assert s.is_listening


def test_serice(host):
    s = host.service('sql_exporter')

    assert s.is_enabled
    assert s.is_running
