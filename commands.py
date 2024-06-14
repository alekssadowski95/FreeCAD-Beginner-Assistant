
import os

import FreeCAD # noqa
import FreeCADGui # noqa

from assistant import get_under_constrained_sketches, get_over_constrained_sketches, has_open_sketches
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

        FreeCAD.Console.PrintMessage("You have referenced a face of your 3D model (topological element) for your sketch: ")
        FreeCAD.Console.PrintMessage("Not implemented yet" + "\n")

        FreeCAD.Console.PrintMessage("You have created a sketch, that is under constrained: ")
        FreeCAD.Console.PrintMessage(str(len(get_under_constrained_sketches(FreeCAD.ActiveDocument)) > 0) + "\n")

        FreeCAD.Console.PrintMessage("You have created a sketch, that is over constrained: ")
        FreeCAD.Console.PrintMessage(str(len(get_over_constrained_sketches(FreeCAD.ActiveDocument)) > 0) + "\n")

        FreeCAD.Console.PrintMessage("Your 3D model is not symmetric in relation to one of the Origin planes: ")
        FreeCAD.Console.PrintMessage("Not implemented yet" + "\n")

        FreeCAD.Console.PrintMessage("You have created a complex sketch that uses a lot of geometrical elements and constraints: ")
        FreeCAD.Console.PrintMessage("Not implemented yet" + "\n")

        FreeCAD.Console.PrintMessage("You have not given your sketch a useful name: ")
        FreeCAD.Console.PrintMessage("Not implemented yet" + "\n")

        FreeCAD.Console.PrintMessage("Your file size is getting large: ")
        FreeCAD.Console.PrintMessage("Not implemented yet" + "\n")

        FreeCAD.Console.PrintMessage("You have created a new document that might not be using version control: ")
        FreeCAD.Console.PrintMessage("Not implemented yet" + "\n")

        FreeCAD.Console.PrintMessage("Your document contains at least one error: ")
        FreeCAD.Console.PrintMessage("Not implemented yet" + "\n")

        FreeCAD.Console.PrintMessage("Your Part Design body contains many features: ")
        FreeCAD.Console.PrintMessage("Not implemented yet" + "\n")

        FreeCAD.Console.PrintMessage("Your system will soon run out of memory: ")
        FreeCAD.Console.PrintMessage("Not implemented yet" + "\n")

        FreeCAD.Console.PrintMessage("Your system cpu usage is very high: ")
        FreeCAD.Console.PrintMessage("Not implemented yet" + "\n")

        FreeCAD.Console.PrintMessage("Your system will soon run out of disk space: ")
        FreeCAD.Console.PrintMessage("Not implemented yet" + "\n")

        FreeCAD.Console.PrintMessage("Your FreeCAD program version is not up to date: ")
        FreeCAD.Console.PrintMessage("Not implemented yet" + "\n")

        FreeCAD.Console.PrintMessage("You have not saved your document in a while: ")
        FreeCAD.Console.PrintMessage("Not implemented yet" + "\n")

        FreeCAD.Console.PrintMessage("You have created a sketch that does not contain a closed wire: ")
        FreeCAD.Console.PrintMessage(str(has_open_sketches(FreeCAD.ActiveDocument)) + "\n")

        FreeCAD.Console.PrintMessage("You have created an additive Part Design feature after a subtractive one: ")
        FreeCAD.Console.PrintMessage("Not implemented yet" + "\n")

        FreeCAD.Console.PrintMessage("You have saved your FreeCAD document using a name that is not compatible with the Linux operating system: ")
        FreeCAD.Console.PrintMessage("Not implemented yet" + "\n")

        FreeCAD.Console.PrintMessage("Your sketch or feature geometry intersects itself, leading to invalid geometry: ")
        FreeCAD.Console.PrintMessage("Not implemented yet" + "\n")

        FreeCAD.Console.PrintMessage("You have used a non-standard file format to save your part: ")
        FreeCAD.Console.PrintMessage("Not implemented yet" + "\n")

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
