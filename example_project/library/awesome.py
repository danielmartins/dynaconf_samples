from dynaconf import settings


def amazing_function():
    print(settings.TO_OVERRIDE_CONF)


if __name__ == "__main__":
    amazing_function()
