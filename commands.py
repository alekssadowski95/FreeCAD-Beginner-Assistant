
import os

import FreeCAD # noqa
import FreeCADGui # noqa

from assistant import get_under_constrained_sketches, get_over_constrained_sketches
from config import addon_work_dir


class AnalyseDocumentCommand:
    """Explanation of the UnderConstrainedSketchCommand command."""

    def __init__(self):
        """Initialize variables for the command that must exist at all times."""
        pass

    def GetResources(self):
        """Return a dictionary with data that will be used by the button or menu item."""
        return {'Pixmap': os.path.join(addon_work_dir, 'icons', 'business.png'),
                'Accel': "Ctrl+A",
                'MenuText': "AnalyseDocumentCommand",
                'ToolTip': "AnalyseDocumentCommand ToolTip"}

    def Activated(self):
        """Run the following code when the command is activated (button press)."""

        if FreeCAD.ActiveDocument == None:
            FreeCAD.Console.PrintMessage("There is no active FreeCAD document." + "\n")
            return
        
        FreeCAD.Console.PrintMessage("\n")
        FreeCAD.Console.PrintMessage("**FreeCAD Beginner Assistant**" + "\n")
        FreeCAD.Console.PrintMessage("--------------------------" + "\n")
        FreeCAD.Console.PrintMessage("Analysing active document <" + FreeCAD.ActiveDocument.Name + ">:" + "\n")

        FreeCAD.Console.PrintMessage("Document has under-constrained sketches: ")
        FreeCAD.Console.PrintMessage(str(len(get_under_constrained_sketches()) > 0) + "\n")

        FreeCAD.Console.PrintMessage("Document has over-constrained sketches: ")
        FreeCAD.Console.PrintMessage(str(len(get_over_constrained_sketches()) > 0) + "\n")

        FreeCAD.Console.PrintMessage("--------------------------" + "\n")



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
        return {'Pixmap': os.path.join(addon_work_dir, 'icons', 'circle-blue.svg'),
                'Accel': "Ctrl+S",
                'MenuText': "OverConstrainedSketchCommand",
                'ToolTip': "OverConstrainedSketchCommand ToolTip"}

    def Activated(self):
        """Run the following code when the command is activated (button press)."""
        print('OverConstrainedSketchCommand activated' + "\n")

    def IsActive(self):
        """Return True when the command should be active or False when it should be disabled (greyed)."""
        return True
