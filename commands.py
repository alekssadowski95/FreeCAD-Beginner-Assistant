
import os

import FreeCAD # noqa
import FreeCADGui # noqa

from assistant import get_under_constrained_sketches, get_over_constrained_sketches, has_open_sketches, has_complex_bodies, has_old_freecad_version
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
        FreeCAD.Console.PrintMessage(str(has_complex_bodies(FreeCAD.ActiveDocument)) + "\n")

        FreeCAD.Console.PrintMessage("Your system will soon run out of memory: ")
        FreeCAD.Console.PrintMessage("Not implemented yet" + "\n")

        FreeCAD.Console.PrintMessage("Your system cpu usage is very high: ")
        FreeCAD.Console.PrintMessage("Not implemented yet" + "\n")

        FreeCAD.Console.PrintMessage("Your system will soon run out of disk space: ")
        FreeCAD.Console.PrintMessage("Not implemented yet" + "\n")

        FreeCAD.Console.PrintMessage("Your FreeCAD program version is not up to date: ")
        FreeCAD.Console.PrintMessage(str(has_old_freecad_version()) + "\n")

        FreeCAD.Console.PrintMessage("You have not saved your document in a while: ")
        FreeCAD.Console.PrintMessage("Not implemented yet" + "\n")

        FreeCAD.Console.PrintMessage("You have created a sketch that does not contain a closed wire: ")
        FreeCAD.Console.PrintMessage(str(has_open_sketches (FreeCAD.ActiveDocument)) + "\n")

        FreeCAD.Console.PrintMessage("You have created an additive Part Design feature after a subtractive one: ")
        FreeCAD.Console.PrintMessage("Not implemented yet" + "\n")

        FreeCAD.Console.PrintMessage("You have saved your FreeCAD document using a name that is not compatible with the Linux operating system: ")
        FreeCAD.Console.PrintMessage("Not implemented yet" + "\n")

        FreeCAD.Console.PrintMessage("Your sketch or feature geometry intersects itself, leading to invalid geometry: ")
        FreeCAD.Console.PrintMessage("Not implemented yet" + "\n")

        FreeCAD.Console.PrintMessage("You have used a non-standard file format to save your part: ")
        FreeCAD.Console.PrintMessage("Not implemented yet" + "\n")

        FreeCAD.Console.PrintMessage("--------------------------" + "\n")

        from datetime import date

        # Get today's date
        today = date.today()

        # Get filename of active freecad document
        filename = FreeCAD.ActiveDocument.Name + ".FCStd"

        # Set 3D view to Isometric
        FreeCADGui.activeDocument().activeView().viewIsometric()

        # Fit the 3D view to content
        FreeCADGui.SendMsgToActiveView("ViewFit")

        # Save the screenshot to a file
        screenshot_abs_path = FreeCADGui.activeDocument().activeView().saveImage('C:/Users/Aleksander/Desktop/test.png',1543,558,'Transparent')

        # Get the rank for this analysis
        rank = get_rank(pts_reached, pts_available)

        result = {
            "date" : today,
            "file" : filename,
            "screenshot" : screenshot_abs_path,
            "pts-reached" : "14",
            "pts-available" : "21",
            "rank" : rank,
            "best-practices" : ()
        }

        best_practices = result["best-practices"]
        best_practices.append(
            {
            "id" : 1,
            "action" : "You have referenced a face of your 3D model (topological element) for your sketch.",
            "effect" : "This might lead to the sketch losing its reference, when the topological elements change.",
            "solution" : "Reference one of the Origin planes or create a new plane, that also only references one of the Origin planes instead.",
            "status" : "Passed"
            }
        )



    def IsActive(self):
        """Return True when the command should be active or False when it should be disabled (greyed)."""
        return True
    
def get_rank(pts_reached, pts_available):
    ratio = pts_reached/pts_available
    if ratio <= 0.5:
        return "Future expert"
    if ratio > 0.5 and ratio <= 0.7:
        return "Bronze"
    if ratio > 0.7 and ratio <= 0.8:
        return "Silver"
    if ratio > 0.8 and ratio <= 0.9:
        return "Gold"
    if ratio > 0.9 and ratio <= 0.95:
        return "Diamond"
    if ratio > 0.95:
        return "Master"


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
