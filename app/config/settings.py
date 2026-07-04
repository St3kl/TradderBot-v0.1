import yaml


class Settings:

    def __init__(self):

        with open("config.yaml", "r") as file:

            self.config = yaml.safe_load(file)

    def get(self, *keys):

        value = self.config

        for key in keys:

            value = value[key]

        return value


settings = Settings()