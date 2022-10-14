import os

######## PLUGINS_PATHS - MID
from .lib import get_plugins_path
######## PLUGINS_PATHS - END

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
######## PLUGINS_PATHS - BEGIN
#PLUGINS_DIR = os.path.join(PACKAGE_DIR, "plugins")
######## PLUGINS_PATHS - MID
PLUGINS_DIR = get_plugins_path(None, PACKAGE_DIR)
######## PLUGINS_PATHS - END
