Example database lib
--------------------
Example lib, contains database driver classes.

usage:
`from pymono.database import Postgres`

structure:
- /pymono: this empty directy defines the global namespace of the project.
  - /database: this subdirectory under pymono/ contains the actual python module and code.
- pyproject.toml: the poetry project file. The important line is `packages = [{ include = "pythonmono/database" }]` which includes the module into the main project's scope.