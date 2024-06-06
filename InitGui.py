# FreeCAD-Beginner-Assistant Addon for FreeCAD
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA

import os

import FreeCAD
import FreeCADGui


class UselessBoxCommand:
    """Explanation of the UselessBoxCommand command."""

    def __init__(self):
        """Initialize variables for the command that must exist at all times."""
        pass

    def GetResources(self):
        """Return a dictionary with data that will be used by the button or menu item."""
        return {'Pixmap': os.path.join(os.path.dirname(__file__), 'icons', 'circle-blue.svg'),
                'Accel': "Ctrl+A",
                'MenuText': "UselessBox",
                'ToolTip': "This is a Useless Box"}

    def Activated(self):
        """Run the following code when the command is activated (button press)."""
        print('UselessBoxOnPointCommand activated')

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
        return {'Pixmap': os.path.join(os.path.dirname(__file__), 'icons', 'circle-blue.svg'),
                'Accel': "Ctrl+S",
                'MenuText': "UselessBoxOnPoint",
                'ToolTip': "This is a Useless Box at a Point"}

    def Activated(self):
        """Run the following code when the command is activated (button press)."""
        print('UselessBoxOnPointCommand activated')

    def IsActive(self):
        """Return True when the command should be active or False when it should be disabled (greyed)."""
        return True

class UselessCylinderCommand:
    """Explanation of the UselessCylinderCommand command."""

    def __init__(self):
        """Initialize variables for the command that must exist at all times."""
        pass

    def GetResources(self):
        """Return a dictionary with data that will be used by the button or menu item."""
        return {'Pixmap': os.path.join(os.path.dirname(__file__), 'icons', 'circle-blue.svg'),
                'Accel': "Ctrl+D",
                'MenuText': "UselessCylinder",
                'ToolTip': "This is a Useless Cylinder"}

    def Activated(self):
        """Run the following code when the command is activated (button press)."""
        print('UselessCylinderCommand activated')

    def IsActive(self):
        """Return True when the command should be active or False when it should be disabled (greyed)."""
        return True

class UselessWorkbench(FreeCADGui.Workbench):
    """Purpose and functionality of the UselessWorkbench."""

    def __init__(self):
        self.__class__.MenuText = "Useless Workbench"
        self.__class__.ToolTip = "A description of the Useless workbench"
        self.__class__.Icon = os.path.join(os.path.dirname(__file__), 'icons', 'circle-blue.svg'),

    def Initialize(self):
        """This function is executed when the workbench is first activated.
        It is executed once in a FreeCAD session followed by the Activated function.
        """

        # Adds commands to the Gui using the Command classes
        FreeCADGui.addCommand('Useless_Box_Command', UselessBoxCommand())
        FreeCADGui.addCommand('UselessBox_On_Point_Command', UselessBoxOnPointCommand())
        FreeCADGui.addCommand('Useless_Cylinder_Command', UselessCylinderCommand())
        
        # A list of command names created above
        self.uselesscommands = [
            "Useless_Box_Command", 
            "UselessBox_On_Point_Command", 
            "Useless_Cylinder_Command"
            ] 
        
        # Adds the list of commands to a new toolbar
        self.appendToolbar("Useless Commands", self.uselesscommands)

         # Adds the list of commands to a new menu
        self.appendMenu("Useless", self.uselesscommands)

        FreeCAD.Console.PrintMessage("Initializing Useless workbench")

    def Activated(self):
        """This function is executed whenever the workbench is activated"""
        FreeCAD.Console.PrintMessage("Activating Useless workbench")

    def Deactivated(self):
        """This function is executed whenever the workbench is deactivated"""
        FreeCAD.Console.PrintMessage("Deactivating Useless workbench")

    def ContextMenu(self, recipient):
        """This function is executed whenever the user right-clicks on screen"""
        # "recipient" will be either "view" or "tree"
        self.appendContextMenu("Useless commands", self.list) # add commands to the context menu
        FreeCAD.Console.PrintMessage("Activating Useless workbench context menu")

    def GetClassName(self): 
        # This function is mandatory if this is a full Python workbench
        # This is not a template, the returned string should be exactly "Gui::PythonWorkbench"
        return "Gui::PythonWorkbench"   

FreeCADGui.addWorkbench(UselessWorkbench())
