from os.path import dirname

from dynaconf import LazySettings
import library

lib_settings_abs_path = dirname(library.__file__) + "/" + "settings.yaml"

settings = LazySettings(
    DEBUG_LEVEL_FOR_DYNACONF="DEBUG",
    PRELOAD_FOR_DYNACONF=[lib_settings_abs_path],
)
