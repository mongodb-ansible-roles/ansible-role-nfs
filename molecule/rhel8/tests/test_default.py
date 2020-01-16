import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_nfs_utils_installed(host):
    assert host.package("nfs-utils").is_installed
    assert host.package("nfs-utils").version == "2.3.3"


def test_nfsstat_in_path(host):
    assert host.exists("nfsstat")
    cmd = host.run("nfsstat --version")
    assert cmd.stdout == "nfsstat: 2.3.3\n"
