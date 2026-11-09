# JupyterLab on Scalingo

This repository contains code used to demonstrate how to deploy [JupyterLab]
on [Scalingo]:

- `jupyter_notebook_config.py` -- Contains the configuration of JupyterLab.
- `Procfile` -- Defines two process types to run JupyterLab:
  - `postdeploy`: initializes the database if required;
  - `web`: main process type, effectively runs JupyterLab.
- `.profile.d/010-jupyterlab.sh` -- Ensures some required environment variable
  are available and well set at runtime.
- `.python-version`, `pyproject.toml`, `uv.lock` -- Define project and
  dependencies.

## Documentation

See the official demo:
👉 https://doc.scalingo.com/tutorials/jupyterlab

## Maintenance Status

This repository is provided for demonstration purposes only. It is not
maintained as a supported Scalingo product, reference implementation or
tutorial. **Scalingo does not guarantee** that it works continuously, remains
compatible over time, or is suitable for production usage.

The demo may include external dependencies not maintained by Scalingo.
Customers are solely responsible for validating all aspects (code, security,
compliance, operations), applying JupyterLab upgrades and security patches by
updating the `pyproject.toml` file accordingly, and redeploying the application
before any production use.


[JupyterLab]: https://jupyter.org/
[Scalingo]: https://scalingo.com/
