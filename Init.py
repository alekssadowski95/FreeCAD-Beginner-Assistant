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


# This will be executed, when FreeCAD is run withou the GUI

import FreeCAD # noqa

# Print normal text to "Report View" console 
print("Print: Hello, World!")

# Print normal text to "Report View" console 
FreeCAD.Console.PrintMessage("Message: Hello, World!" + "\n")

# Print orange Warning text to "Report View" console 
FreeCAD.Console.PrintWarning("Warning: Hello, World!" + "\n")

# Print red error text to "Report View" console 
FreeCAD.Console.PrintError("Error: Hello, World!" + "\n")