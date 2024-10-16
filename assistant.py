from datetime import datetime

import FreeCAD  # noqa
import FreeCADGui  # noqa
import Sketcher  # noqa
import os
import sys

Path = os.path.join(os.path.dirname(__file__))
PathImages = os.path.join(Path, "model_images")
PathIcons = os.path.join(Path, "icons")
PathScreenshots = os.path.join(Path, "Screenshots")
PathDocs = os.path.join(Path, "Docs")
PathReports = os.path.join(Path, "reports_pdf")
sys.path.append(Path)
sys.path.append(PathImages)
sys.path.append(PathIcons)
sys.path.append(PathScreenshots)
sys.path.append(PathDocs)
sys.path.append(PathReports)

""" From own testing:

When sketches in FreeCAD are underconstrained, sketch.FullyConstrained returns False
When sketches in FreeCAD are underconstrained, sketch.solve() returns 0
When sketches in FreeCAD are overconstrained, sketch.FullyConstrained returns True
When sketches in FreeCAD are overconstrained, sketch.solve() returns -2
"""

""" From FreeCAD Documentation:

solve()

int SketchObject::solve( bool updateGeoAfterSolving = true	)
          	
solves the sketch and updates the geometry, but not all the dependent features (does not recompute) When a recompute is necessary, recompute triggers execute() which solves the sketch and updates all dependent features When a solve only is necessary (e.g.

DoF changed), solve() solves the sketch and updates the geometry (if updateGeoAfterSolving==true), but does not trigger any recompute.

Returns
    0 if no error, if error, the following codes in this order of priority: -4 if overconstrained, -3 if conflicting, -1 if solver error, -2 if redundant constraints 
"""


# ID 1: You have referenced a face of your 3D model (topological element) for your sketch.
def has_referenced_face_for_sketch():
    result = {
        "id": 1,
        "action": "You have referenced a face of your 3D model (topological element) for your sketch.",
        "effect": "This might lead to the sketch losing its reference, when the topological elements change.",
        "solution": "Reference one of the Origin planes or create a new plane, that also only references one of the Origin planes instead.",
        "status": "Unchecked",
    }
    return result


# ID 2: You have created a sketch, that is under constrained.
def has_under_constrained_sketch(doc: FreeCAD.Document):
    result = {
        "id": 2,
        "action": "You have created a sketch, that is under constrained.",
        "effect": "This might lead to unexpected behaviour, when you use that sketch for a feature.",
        "solution": "Go back to your sketch and fully define it using dimensional of geometrical constraints.",
        "status": "Unchecked",
    }
    if len(get_under_constrained_sketches(doc)) > 0:
        result["status"] = "Failed"
        return result
    else:
        result["status"] = "Passed"
        return result


# ID 3: You have created a sketch, that is over constrained.
def has_over_constrained_sketch(doc: FreeCAD.Document):
    result = {
        "id": 3,
        "action": "You have created a sketch, that is over constrained.",
        "effect": "This might lead to unexpected behaviour, when you use that sketch for a feature.",
        "solution": "Go back to your sketch and remove redundant constraints.",
        "status": "Unchecked",
    }
    if len(get_over_constrained_sketches(doc)) > 0:
        result["status"] = "Failed"
        return result
    else:
        result["status"] = "Passed"
        return result


# ID 4: Your 3D model is not symmetric in relation to one of the Origin planes.
def is_body_not_symmetric():
    result = {
        "id": 4,
        "action": "Your 3D model is not symmetric in relation to one of the Origin planes.",
        "effect": "Designing your 3D model symmetric to as many Origin planes as possible makes it easier to modify it in the future.",
        "solution": "Try to create your 3D model symmetric in relation to as many Origin planes as possible.",
        "status": "Unchecked",
    }
    return result


# ID 5: You have created a complex sketch that uses a lot of geometrical elements and constraints.
def has_complex_sketch():
    result = {
        "id": 5,
        "action": "You have created a complex sketch that uses a lot of geometrical elements and constraints.",
        "effect": "This might lead to performance issues and make building your 3D model slow.",
        "solution": "Split up your complex sketch into multiple simple sketches if possible.",
        "status": "Unchecked",
    }
    return result


# ID 6: You have not given your sketch a meaningful name.
def has_not_meaningful_sketch_name():
    result = {
        "id": 6,
        "action": "You have not given your sketch a meaningful name.",
        "effect": "This might lead to you getting confused when trying to reference a specific sketch in a formula or selecting it for a feature.",
        "solution": "Rename your sketch to something that represents its purpose.",
        "status": "Unchecked",
    }
    return result


# ID 7: Your file size is getting large.
def is_file_size_large():
    result = {
        "id": 7,
        "action": "Your file size is getting large.",
        "effect": "This might lead to stability issues and the program crashing.",
        "solution": "Save your document regularily.",
        "status": "Unchecked",
    }
    return result


# ID 8: You have created a new document that might not be using version control.
def is_not_version_controled():
    result = {
        "id": 8,
        "action": "You have created a new document that might not be using version control.",
        "effect": "Using version control for your documents will help you keep track of your document progress. Also, in combination with a secure hosting service, this prevents you from losing data.",
        "solution": "Use a version control, like git or Subversion. To host your files using git you can use Github.",
        "status": "Unchecked",
    }
    return result


# ID 9: Your document contains at least one error.
def has_doc_errors():
    result = {
        "id": 9,
        "action": "Your document contains at least one error.",
        "effect": "This might lead to unexpected behaviour of your 3D model or the program even crashing.",
        "solution": "Resolve all errors first, before continuing with your work on this document. Thank me later.",
        "status": "Unchecked",
    }
    return result


# ID 10: Your Part Design body contains many features.
def has_complex_bodies(doc: FreeCAD.Document):
    result = {
        "id": 10,
        "action": "Your Part Design body contains many features.",
        "effect": "This might lead to the 3D model being hard to understand and might potentially lead to performance issues.",
        "solution": "Try to combine features, especially the ones dependent on sketches.",
        "status": "Unchecked",
    }
    bodies = get_objects_by_type_id(doc, "PartDesign::Body")
    for body in bodies:
        if body_has_many_features(body):
            return True
    return False


# ID 11: Your system will soon run out of memory.
# TODO: Requires 'psutil' library, which is not included with the Python interpreter integrated in FreeCAD
def high_ram_usage():
    result = {
        "id": 11,
        "action": "Your system will soon run out of memory.",
        "effect": "This might lead to the program crashing or dramatically slowing down.",
        "solution": "Free up some memory by closing other programs or files that you don't need right now.",
        "status": "Unchecked",
    }
    return result


# ID 12: Your system cpu usage is very high.
# TODO: Requires 'psutil' library, which is not included with the Python interpreter integrated in FreeCAD
def high_cpu_usage():
    result = {
        "id": 12,
        "action": "Your system cpu usage is very high.",
        "effect": "This might lead to the program crashing or dramatically slowing down.",
        "solution": "Free up some cpu resources by closing other programs or files that you don't need right now.",
        "status": "Unchecked",
    }
    return result


# ID 13: Your system will soon run out of disk space.
# TODO: Requires 'psutil' library, which is not included with the Python interpreter integrated in FreeCAD
def high_disk_usage():
    result = {
        "id": 13,
        "action": "Your system will soon run out of disk space.",
        "effect": "This might lead to you not being able to save your document.",
        "solution": "Free up some disk space by deleting or moving files that you don't need.",
        "status": "Unchecked",
    }
    return result


# ID 14: Your FreeCAD program version is not up to date.
def has_old_freecad_version():
    """Check if FreeCAD version is up to date."""
    result = {
        "id": 14,
        "action": "Your FreeCAD program version is not up to date.",
        "effect": "This might not only prevent you from using the newest features but also usability and stability improvements in existing features.",
        "solution": "Install the newest stable version of FreeCAD. You can go back to this version and use both side by side.",
        "status": "Unchecked",
    }
    major = 0
    minor = 21
    patch = 2
    version_info = FreeCAD.Version()
    if version_info[0] < major:
        return True
    if version_info[1] < minor:
        return True
    if version_info[2] < patch:
        return True
    return False


# ID 15: You have not saved your document in a while.
# TODO: Might not work as intended.
def doc_was_not_saved_recently(doc: FreeCAD.Document):
    """Checks how long ago the document was modified."""
    result = {
        "id": 15,
        "action": "You have not saved your document in a while.",
        "effect": "This might lead to you losing your progress if the program crashes.",
        "solution": "Save your document now. You can also enable auto-save, to let FreeCAD take care of that.",
        "status": "Unchecked",
    }
    if doc.isSaved():
        return False
    date_string = doc.LastModifiedDate
    date_format = "%Y-%m-%dT%H:%M:%SZ"
    date_object = datetime.strptime(date_string, date_format)
    current_time = datetime.now()
    delta = current_time - date_object
    if delta.total_seconds() > 300:
        return True
    return False


# ID 16: You have created a sketch that does not contain a closed wire.
def has_sketch_open_wire(sketch: Sketcher.Sketch):
    """Returns true if sketch contains an open wire"""
    wires = sketch.Shape.Wires
    for wire in wires:
        if wire.isClosed() == False:
            return True
    return False


def has_open_sketches(doc: FreeCAD.Document):
    """Returns true if document contains at least one sketch with an open wire"""
    result = {
        "id": 16,
        "action": "You have created a sketch that does not contain a closed wire.",
        "effect": "This will lead to creating a zero thickness surface instead of a solid.",
        "solution": "When creating solids, always close your wires in your sketch.",
        "status": "Unchecked",
    }
    sketches = get_sketches(doc)
    for sketch in sketches:
        if has_sketch_open_wire(sketch):
            return True
    return False


# ID 17: You have created an additive Part Design feature after a subtractive one.
def has_additive_after_subtractive_all(doc: FreeCAD.Document):
    result = {
        "id": 17,
        "action": "You have created an additive Part Design feature after a subtractive one.",
        "effect": "This might prevent you from staying flexible in your modeling approach.",
        "solution": "If possible, first create all additive Part Design features and then all the subtractive ones.",
        "status": "Unchecked",
    }
    bodies = get_objects_by_type_id(doc, "PartDesign::Body")
    for body in bodies:
        if has_additive_after_subtractive(body):
            return True
    return False


# ID 18: You have created a Part Design feature after a fillet or chamfer.


# ID 19: You have saved your FreeCAD document using a name that is not compatible with the Linux operating system.
# TODO: Requires 'pathvalidate' library, which is not included with the Python interpreter integrated in FreeCAD
def has_valid_filename():
    result = {
        "id": 19,
        "action": "You have saved your FreeCAD document using a name that is not compatible with the Linux operating system.",
        "effect": "This might lead to other FreeCAD users not being able to open your file when using Linux.",
        "solution": "Rename your FreeCAD document to something that's compatible with Linux. Use underscores or hyphens for multipart names (e.g. 'my-own-spaceship.FCStd'). Remember that Linux is case-sensitive.",
        "status": "Unchecked",
    }
    return result


# ID 20: Your sketch intersects itself, leading to invalid geometry.
def check_if_edges_intersect(edge1, edge2):
    """
    Check if two edges in FreeCAD intersect.

    Args:
    edge1: First edge (Part.Edge)
    edge2: Second edge (Part.Edge)

    Returns:
    bool: True if edges intersect, otherwise False.
    """
    result = {
        "id": 20,
        "action": "Your sketch or feature geometry intersects itself, leading to invalid geometry.",
        "effect": "This can lead to errors in operations that depend on that sketch or feature.",
        "solution": "Modify the sketch or feature to remove or resolve the intersecting geometry.",
        "status": "Unchecked",
    }
    # Get the shape of the edges
    shape1 = edge1.Shape
    shape2 = edge2.Shape

    # Perform intersection check
    common = shape1.common(shape2)

    # Check if the common shape has vertices, which means they intersect
    if common.Vertexes:
        return True
    else:
        return False


# ID 21: You have used a non-standard file format to save your part.
def is_export_standard_format():
    result = {
        "id": 21,
        "action": "You have used a non-standard file format to save your part.",
        "effect": "This can create compatibility issues when sharing files with others.",
        "solution": "'Export' or 'Save As' your part in a standard file format.",
        "status": "Unchecked",
    }
    return result


#
# Helper methods
#
def get_objects_by_type_id(doc: FreeCAD.Document, type_id: str):
    """Returns all objects of a given type from a FreeCAD document

    # TypeId
    # origin:               'App::Origin'
    # origin-line:          'App::Line'
    # origin-plane:         'App::Plane'
    # sketch:               'Sketcher::SketchObject'
    # pd-body:              'PartDesign::Body'
    # pd-coordinate system: 'PartDesign::CoordinateSystem'
    # pd-datum plane:       'PartDesign::Plane'
    # pd-datum line:        'PartDesign::Line'
    # pd-datum point:       'PartDesign::Point'
    # pd-pad:               'PartDesign::Pad'
    # pd-pocket:            'PartDesign::Pocket'
    # pd-fillet:            'PartDesign::Fillet'
    # pd-chamfer:           'PartDesign::Chamfer'

    """
    objects = []
    for obj in doc.Objects:
        if obj.TypeId == type_id:
            objects.append(obj)

    if not objects:
        print("No object of given type found in the document")
        return
    return objects


def get_over_constrained_sketches(doc: FreeCAD.Document):
    """Returns all over-constrained sketches from the active FreeCAD document"""
    sketches = get_sketches(doc)
    over_constrained_sketches = []
    for sketch in sketches:
        if sketch.FullyConstrained == True and sketch.solve() != 0:
            over_constrained_sketches.append(sketch)
    return over_constrained_sketches


def get_under_constrained_sketches(doc: FreeCAD.Document):
    """Returns all under-constrained sketches from the active FreeCAD document"""
    sketches = get_sketches(doc)
    under_constrained_sketches = []
    for sketch in sketches:
        if sketch.FullyConstrained == False and sketch.solve() == 0:
            under_constrained_sketches.append(sketch)
    return under_constrained_sketches


def get_sketches(doc: FreeCAD.Document):
    """Returns all sketches from a FreeCAD document"""
    type_id = "Sketcher::SketchObject"
    sketches = []
    for obj in doc.Objects:
        if obj.TypeId == type_id:
            sketches.append(obj)
    return sketches


def body_has_many_features(body, limit: int = 8):
    if len(body.Group) > limit:
        return True
    return False


def has_additive_after_subtractive(body):
    additive_features_type_id = [
        "PartDesign::Pad",
        "PartDesign::Revolution",
        "PartDesign::AdditivePipe",
        "PartDesign::AdditiveLoft",
        "PartDesign::AdditiveBox",
        "PartDesign::AdditiveCylinder",
        "PartDesign::AdditiveSphere",
        "PartDesign::AdditiveCone",
        "PartDesign::AdditiveTorus",
        "PartDesign::AdditivePrism",
        "PartDesign::AdditiveHelix",
    ]
    subtractive_features_type_id = [
        "PartDesign::Pocket",
        "PartDesign::Groove",
        "PartDesign::SubtractivePipe",
        "PartDesign::SubtractiveLoft",
        "PartDesign::SubtractiveBox",
        "PartDesign::SubtractiveCylinder",
        "PartDesign::SubtractiveSphere",
        "PartDesign::SubtractiveCone",
        "PartDesign::SubtractiveTorus",
        "PartDesign::SubtractivePrism",
        "PartDesign::SubtractiveHelix",
    ]
    for add_feature in body.Group:
        if add_feature.TypeId in additive_features_type_id:
            for sub_feature in body.Group:
                if sub_feature.TypeId in subtractive_features_type_id and body.Group.index(
                    add_feature
                ) > body.Group.index(sub_feature):
                    return True
    return False


def get_rank(pts_reached, pts_available):
    ratio = pts_reached / pts_available
    if ratio <= 0.5:
        return "Beginner"
    if ratio > 0.5 and ratio <= 0.7:
        return "Bronze Apprentice"
    if ratio > 0.7 and ratio <= 0.8:
        return "Silver Apprentice"
    if ratio > 0.8 and ratio <= 0.9:
        return "Gold Apprentice"
    if ratio > 0.9 and ratio <= 0.95:
        return "Diamond Apprentice"
    if ratio > 0.95:
        return "Master"


def generate_result_dict(fcstd_file_path=""):
    # Get today's date
    from datetime import datetime

    today = datetime.today()
    print(str(today))

    # Get filename of active freecad document
    filename = FreeCAD.ActiveDocument.Name + ".FCStd"
    print(filename)

    # Set 3D view to Isometric
    FreeCADGui.activeDocument().activeView().viewIsometric()

    # Fit the 3D view to content
    FreeCADGui.SendMsgToActiveView("ViewFit")

    # Save the screenshot to a file
    screenshot = os.path.join(PathImages, "test.png")
    screenshot_abs_path = (
        FreeCADGui.activeDocument()
        .activeView()
        .saveImage(
            screenshot,
            1543,
            822,
            "Transparent",
        )
    )
    print(screenshot_abs_path)

    result_dict = {
        "date": str(today),
        "file": filename,
        "screenshot": screenshot,
        "pts-reached": "not available",
        "pts-available": "not available",
        "rank": "Bronze Apprentice",
        "best-practices": [],
    }

    result_dict["best-practices"].append(has_referenced_face_for_sketch())

    result_dict["best-practices"].append(has_under_constrained_sketch(FreeCAD.ActiveDocument))

    result_dict["best-practices"].append(has_over_constrained_sketch(FreeCAD.ActiveDocument))

    result_dict["best-practices"].append(is_body_not_symmetric())

    result_dict["best-practices"].append(has_complex_sketch())

    result_dict["best-practices"].append(has_not_meaningful_sketch_name())

    result_dict["best-practices"].append(is_not_version_controled())

    result_dict["best-practices"].append(has_doc_errors())

    # Populate points fields in result dict
    pts_reached = 0
    pts_available = 0

    for practice in result_dict["best-practices"]:
        if practice["status"] == "Passed":
            pts_available = pts_available + 1
            pts_reached = pts_reached + 1
        elif practice["status"] == "Failed":
            pts_available = pts_available + 1
        else:
            pass

    result_dict["pts-reached"] = str(pts_reached)
    result_dict["pts-available"] = str(pts_available)

    # Get the rank for this analysis
    rank = get_rank(pts_reached, pts_available)
    result_dict["rank"] = rank

    return result_dict
