from pathlib import Path
import yaml


class ConfigLoader:

    def __init__(self, filename="config/settings.yaml"):

        path = Path(filename)

        with open(path, "r", encoding="utf-8") as f:

            self._config = yaml.safe_load(f)

    def get(self, *keys, default=None):

        value = self._config

        for key in keys:

            if not isinstance(value, dict):

                return default

            value = value.get(key)

            if value is None:

                return default

        return value