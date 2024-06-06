
import os

import FreeCAD # noqa
import FreeCADGui # noqa


class UselessBoxCommand:
    """Explanation of the UselessBoxCommand command."""

    def __init__(self):
        """Initialize variables for the command that must exist at all times."""
        pass

    def GetResources(self):
        """Return a dictionary with data that will be used by the button or menu item."""
        return {'Pixmap': os.path.join(FreeCAD.getHomePath(), 'Mod', 'FreeCAD-Beginner-Assistant', 'icons', 'circle-blue.svg'),
                'Accel': "Ctrl+A",
                'MenuText': "UselessBox",
                'ToolTip': "This is a Useless Box"}

    def Activated(self):
        """Run the following code when the command is activated (button press)."""
        print('UselessBoxOnPointCommand activated' + "\n")

    def IsActive(self):
        """Return True when the command should be active or False when it should be disabled (greyed)."""
        return True

class UselessBoxOnPointCommand:
    """Explanation of the UselessBoxOnPointCommand command."""

    def __init__(self):
        """Initialize variables for the command that must exist at all times."""
        pass

    def GetResources(self):
        """Return a dictionary with data that will be used by the button or menu item."""
        return {'Pixmap': os.path.join(FreeCAD.getHomePath(), 'Mod', 'FreeCAD-Beginner-Assistant', 'icons', 'circle-blue.svg'),
                'Accel': "Ctrl+S",
                'MenuText': "UselessBoxOnPoint",
                'ToolTip': "This is a Useless Box at a Point"}

    def Activated(self):
        """Run the following code when the command is activated (button press)."""
        print('UselessBoxOnPointCommand activated' + "\n")

    def IsActive(self):
        """Return True when the command should be active or False when it should be disabled (greyed)."""
        return True