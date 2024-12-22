"""Verifier module."""


def test_podman_uninstalled(host):
    """Test if podman is uninstalled."""
    command = host.run("which podman")
    assert command.rc != 0
    assert command.stdout == ""
