import os
import importlib


def load_env_vars():
    env: str = os.getenv("APP_SETTINGS_MODULE", ".local")
    module = importlib.import_module(name=env, package="app.config")

    config = {
        name: getattr(module, name) for name in dir(module) if name.isupper()
    }

    return config
