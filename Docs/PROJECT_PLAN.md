# FreeCAD Beginner Assistant
The FreeCAD Beginner Assistant analyses a FreeCAD FCStd File containing at least one Part Design Body and gives realtime or asynchronous recommendations/hints, based on best practices, on what was done well and what can be improved. Aims to increase the quality of community-created Part Design models. This project is related to the FreeCAD-Tutorial-Generator and the FCViewer Platform and adds to the ecosystem of learning resources for Beginner FreeCAD Users.


All best practices with all the required information to implement them get collected in the "freecad-part-design-best-practices.xlsx" spreadsheet.


Types of best practices:
- Preferred ordner of operations
- Preferred use of specific operations over other ones
- Preferred parameters for operations


Each best practice consists of:
  - a title
  - a method that checks if the best practice has been applied
  - a feedback text for success and fail.
    - For success, feedback text consists of a description of the best practice that has been applied and why it's important.
    - For fail, feedback text consists of a description of what could be improved and why its a problem.
- Return score in % and a badge (% intervalls), based on % of best practices that have been applied, each best practice having a weight (0.0 - 1.0, default is 0.5) assigned to them.


-> How does the code structure look like for this application?: Do it like validators are usually implemented, with a class for each best practice, but that would lead to a million classes. Each best practice needs to have at least one method and data for fail and success. What would be a more lightweight structure for that?


Potential sources for more best practices to be integrated in to spreadsheet (remove after integrated): 
- [https://wiki.freecad.org/Best_Practices_with_SpreadSheets](https://wiki.freecad.org/Best_Practices_with_SpreadSheets)
- [https://forum.freecad.org/viewtopic.php?t=12738](https://forum.freecad.org/viewtopic.php?t=12738)
- [https://forum.freecad.org/viewtopic.php?t=15432](https://forum.freecad.org/viewtopic.php?t=15432)
- [https://www.youtube.com/playlist?list=PLP1rv37BojTd5NY3E_aqOWUe0uA8J-J1T](https://www.youtube.com/playlist?list=PLP1rv37BojTd5NY3E_aqOWUe0uA8J-J1T)


## Vision
- Integrate into FCViewer for asynchronous feedback.
- Integrate into FreeCAD for realtime feedback.

-> Increase the quality of community-created Part Design projects.
