import os
import logging

import pyblish.api

from openpype.host import HostBase
from openpype.hosts.webpublisher import WEBPUBLISHER_ROOT_DIR
######## PLUGINS_PATHS - MID
from openpype.lib import get_plugins_path
######## PLUGINS_PATHS - END

log = logging.getLogger("openpype.hosts.webpublisher")


class WebpublisherHost(HostBase):
    name = "webpublisher"

    def install(self):
        print("Installing Pype config...")
        pyblish.api.register_host(self.name)

        ######## PLUGINS_PATHS - BEGIN
        """
        publish_plugin_dir = os.path.join(
            WEBPUBLISHER_ROOT_DIR, "plugins", "publish"
        )
        """
        ######## PLUGINS_PATHS - MID
        #TODO: check/test
        plugins_dir = get_plugins_path(self.name, WEBPUBLISHER_ROOT_DIR)
        publish_plugin_dir = os.path.join(plugins_dir, "publish")
        ######## PLUGINS_PATHS - END
        pyblish.api.register_plugin_path(publish_plugin_dir)
        self.log.info(publish_plugin_dir)
