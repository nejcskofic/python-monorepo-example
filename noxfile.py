import os
import nox

os.environ.update({"PDM_IGNORE_SAVED_PYTHON": "1"})


@nox.session()
@nox.parametrize("package", ["a", "b", "c", "d", "e"])
def test(session: nox.Session, package: str):
    session.run("pdm", "install", "-dG", "test", "--no-self", "--no-default", external=True)

    with session.chdir(f"packages/{package}"):
        session.run("pdm", "install", "--prod", "--no-editable", external=True)
        session.run("pytest", "tests")
