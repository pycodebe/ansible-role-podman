# cSpell:disable
"""Verifier module."""


def test_podman_registry(host):
    """Test if Docker Hub registry is configured in Podman."""

    registries_conf = host.file("/root/.config/containers/registries.conf")
    assert registries_conf.exists
    assert (
        'unqualified-search-registries = ["docker.io"]'
        in registries_conf.content_string
    )
    assert "[[registry]]" in registries_conf.content_string
    assert 'location = "docker.io"' in registries_conf.content_string

    command = host.run("podman info --format '{% raw %}{{.Registries}}{% endraw %}'")
    assert command.rc == 0
    assert "docker.io" in command.stdout
