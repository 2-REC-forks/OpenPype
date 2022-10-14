import os


def env_value_to_bool(env_key=None, value=None, default=False):
    """Convert environment variable value to boolean.

    Function is based on value of the environemt variable. Value is lowered
    so function is not case sensitive.

    Returns:
        bool: If value match to one of ["true", "yes", "1"] result if True
            but if value match to ["false", "no", "0"] result is False else
            default value is returned.
    """
    if value is None and env_key is None:
        return default

    if value is None:
        value = os.environ.get(env_key)

    if value is not None:
        value = str(value).lower()
        if value in ("true", "yes", "1", "on"):
            return True
        elif value in ("false", "no", "0", "off"):
            return False
    return default


def get_paths_from_environ(env_key=None, env_value=None, return_first=False):
    """Return existing paths from specific environment variable.

    Args:
        env_key (str): Environment key where should look for paths.
        env_value (str): Value of environment variable. Argument `env_key` is
            skipped if this argument is entered.
        return_first (bool): Return first found value or return list of found
            paths. `None` or empty list returned if nothing found.

    Returns:
        str, list, None: Result of found path/s.
    """
    existing_paths = []
    if not env_key and not env_value:
        if return_first:
            return None
        return existing_paths

    if env_value is None:
        env_value = os.environ.get(env_key) or ""

    path_items = env_value.split(os.pathsep)
    for path in path_items:
        # Skip empty string
        if not path:
            continue
        # Normalize path
        path = os.path.normpath(path)
        # Check if path exists
        if os.path.exists(path):
            # Return path if `return_first` is set to True
            if return_first:
                return path
            # Store path
            existing_paths.append(path)

    # Return None if none of paths exists
    if return_first:
        return None
    # Return all existing paths from environment variable
    return existing_paths

######## PLUGINS_PATHS - MID
def get_plugins_env():
    """Gets the plugins path from environment or settings"""
    plugin_env = os.getenv("OPENPYPE_PLUGINS_DIR")
    if plugin_env:
        return plugin_env

    studio_extra_path = os.getenv("STUDIO_EXTRA_PATH")
    if not studio_extra_path:
        import platform
        from openpype.settings import get_system_settings
        settings = get_system_settings()
        sys_name = platform.system().lower()
        studio_extra_path = settings["general"]["studio_extra_path"][sys_name]

    if studio_extra_path:
        # 'str' required to avoid unicode problems with Pyblish
        #TODO(derek): Should be changed/fixed in Pyblish?
        plugin_env = os.path.join(str(studio_extra_path), "plugins")

    return plugin_env


def get_plugins_path(host_name, host_path):
    """Gets the plugins path for a specific host"""
    plugin_env = get_plugins_env()
    if plugin_env and os.path.exists(plugin_env):
        if host_name:
            plugins_path = os.path.join(plugin_env,
                                        "hosts",
                                        host_name,
                                        "plugins")
            if os.path.exists(plugins_path):
                return plugins_path

            # Look in "modules" if not found in "hosts"
            plugins_path = os.path.join(plugin_env,
                                        "modules",
                                        host_name,
                                        "plugins")
            if os.path.exists(plugins_path):
                return plugins_path

        else:
            plugins_path = os.path.join(plugin_env,
                                        "openpype",
                                        "plugins")
            if os.path.exists(plugins_path):
                return plugins_path

    # Get host plugins path from host file location (OpenPype 'normal' case)
    return os.path.join(host_path, "plugins")
######## PLUGINS_PATHS - END