from avalon import api


class ModelLoader(api.Loader):
    """Load the model"""

    families = ["colorbleed.model"]
    representations = ["ma"]

    label = "Reference Model"
    order = -10
    icon = "code-fork"
    color = "orange"

    def process(self, name, namespace, context, data):

        import maya.cmds as cmds
        from avalon import maya

        with maya.maintained_selection():
            nodes = cmds.file(self.fname,
                              namespace=namespace,
                              reference=True,
                              returnNewNodes=True,
                              groupReference=True,
                              groupName="{}:{}".format(namespace, name))

        self[:] = nodes
