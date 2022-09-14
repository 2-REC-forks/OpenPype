# -*- coding: utf-8 -*-
"""Collect original base name for use in templates."""
from pathlib import Path

import pyblish.api


class CollectOriginalBasename(pyblish.api.InstancePlugin):
    """Collect original file base name."""

    order = pyblish.api.CollectorOrder + 0.498
    label = "Collect Base Name"
    hosts = ["traypublisher"]

    def process(self, instance):

        try:
            file_name = Path(instance.data["representations"][0]["files"])
        except KeyError:
            self.log.info((
                "Representation not found, skipping collection of file "
                "basename."
            ))
        else:
            instance.data["originalBasename"] = file_name.stem
