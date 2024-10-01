
import os

import FreeCAD # noqa
import FreeCADGui # noqa

from assistant import generate_result_dict
from pdfgen import generate_pdf
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
        
        # 1. generate analysis report dict
        result_dict = generate_result_dict()
        # 2. Generate PDF from report dict and open PDF in default viewer
        generate_pdf(result_dict)

    def IsActive(self):
        """Return True when the command should be active or False when it should be disabled (greyed)."""
        return True
    
