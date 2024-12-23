"""Verifier module."""


def test_podman_installed(host):
    """Test if podman is installed."""
    command = host.run("podman --version")
    assert command.rc == 0
    assert command.stdout.startswith("podman version")
