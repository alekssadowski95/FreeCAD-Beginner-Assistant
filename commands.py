
import os

import FreeCAD # noqa
import FreeCADGui # noqa

from assistant import get_under_constrained_sketches, get_over_constrained_sketches


class UnderConstrainedSketchCommand:
    """Explanation of the UnderConstrainedSketchCommand command."""

    def __init__(self):
        """Initialize variables for the command that must exist at all times."""
        pass

    def GetResources(self):
        """Return a dictionary with data that will be used by the button or menu item."""
        return {'Pixmap': os.path.join(FreeCAD.getHomePath(), 'Mod', 'FreeCAD-Beginner-Assistant', 'icons', 'circle-blue.svg'),
                'Accel': "Ctrl+A",
                'MenuText': "UnderConstrainedSketchCommand",
                'ToolTip': "UnderConstrainedSketchCommand ToolTip"}

    def Activated(self):
        """Run the following code when the command is activated (button press)."""
        print('UnderConstrainedSketchCommand activated' + "\n")
        print(get_under_constrained_sketches())

    def IsActive(self):
        """Return True when the command should be active or False when it should be disabled (greyed)."""
        return True

class OverConstrainedSketchCommand:
    """Explanation of the OverConstrainedSketchCommand command."""

    def __init__(self):
        """Initialize variables for the command that must exist at all times."""
        pass

    def GetResources(self):
        """Return a dictionary with data that will be used by the button or menu item."""
        return {'Pixmap': os.path.join(FreeCAD.getHomePath(), 'Mod', 'FreeCAD-Beginner-Assistant', 'icons', 'circle-blue.svg'),
                'Accel': "Ctrl+S",
                'MenuText': "OverConstrainedSketchCommand",
                'ToolTip': "OverConstrainedSketchCommand ToolTip"}

    def Activated(self):
        """Run the following code when the command is activated (button press)."""
        print('OverConstrainedSketchCommand activated' + "\n")
        print(get_over_constrained_sketches())

    def IsActive(self):
        """Return True when the command should be active or False when it should be disabled (greyed)."""
        return True