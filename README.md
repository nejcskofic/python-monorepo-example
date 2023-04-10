# python-monorepo-example
Python mono repo example using PDM

This repo contains example of how you could structure your monorepo and manage it using PDM. All subpackages are declared under
`/packages` folder. Dependencies are as follows:
- Package a has no dependencies
- Package b depends on a
- Package c depends on b
- Package d depends on c
- Package e depends on a

Root project contains only development level dependencies (such as pytest and nox) and all packages in editable mode.

Each package contains single test verifying that dependency can be called. Nox can be used to run all tests from the root.

PyCharm configuration has also been commited, since PyCharm cannot determine project structure out of other files (yet).
