import nox


@nox.session
def tests(session):
    """Cada sesión crea su ambiente para que la prueba no dependa del equipo."""

    session.install("--requirement", "requirements.txt", "pytest")
    session.run("pytest", "tests/test_activity.py")
