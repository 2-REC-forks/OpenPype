import os
from openpype.modules import OpenPypeModule
from openpype.modules.interfaces import IPluginPaths
######## PLUGINS_PATHS - MID
from openpype.lib import get_plugins_path
######## PLUGINS_PATHS - END

SLACK_MODULE_DIR = os.path.dirname(os.path.abspath(__file__))


class SlackIntegrationModule(OpenPypeModule, IPluginPaths):
    """Allows sending notification to Slack channels during publishing."""

    name = "slack"

    def initialize(self, modules_settings):
        slack_settings = modules_settings[self.name]
        self.enabled = slack_settings["enabled"]

    def get_launch_hook_paths(self):
        """Implementation for applications launch hooks."""

        return os.path.join(SLACK_MODULE_DIR, "launch_hooks")

    def get_plugin_paths(self):
        """Deadline plugin paths."""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ######## PLUGINS_PATHS - BEGIN
        """
        return {
            "publish": [os.path.join(current_dir, "plugins", "publish")]
        }
        """
        ######## PLUGINS_PATHS - MID
        plugins_dir = get_plugins_path(self.name, current_dir)
        return {
            "publish": [os.path.join(plugins_dir, "publish")]
        }
        ######## PLUGINS_PATHS - END
