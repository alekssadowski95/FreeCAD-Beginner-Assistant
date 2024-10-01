from datetime import datetime

import FreeCAD # noqa
import FreeCADGui # noqa
import Sketcher # noqa


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

# ID 2: You have created a sketch, that is under constrained.

# ID 3: You have created a sketch, that is over constrained.

# ID 4: Your 3D model is not symmetric in relation to one of the Origin planes.

# ID 5: You have created a complex sketch that uses a lot of geometrical elements and constraints.

# ID 6: You have not given your sketch a useful name.

# ID 7: Your file size is getting large.

# ID 8: You have created a new document that might not be using version control.

# ID 9: Your document contains at least one error.

# ID 10: Your Part Design body contains many features.
def body_has_many_features(body, limit: int = 8):
    if len(body.Group) > limit:
        return True
    return False

def has_complex_bodies(doc: FreeCAD.Document):
    bodies = get_objects_by_type_id(doc, 'PartDesign::Body')
    for body in bodies:
        if body_has_many_features(body):
            return True
    return False

# ID 11: Your system will soon run out of memory.
# TODO: Requires 'psutil' library, which is not included with the Python interpreter integrated in FreeCAD
def high_ram_usage():
    return NotImplementedError

# ID 12: Your system cpu usage is very high.
# TODO: Requires 'psutil' library, which is not included with the Python interpreter integrated in FreeCAD
def high_cpu_usage():
    return NotImplementedError

# ID 13: Your system will soon run out of disk space.
# TODO: Requires 'psutil' library, which is not included with the Python interpreter integrated in FreeCAD
def high_disk_usage():
    return NotImplementedError

# ID 14: Your FreeCAD program version is not up to date.
def has_old_freecad_version():
    """Check if FreeCAD version is up to date."""
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

# ID 16: You have created a sketch that does not contain a closed wire.

# ID 17: You have created an additive Part Design feature after a subtractive one.
def has_additive_after_subtractive(body):
    additive_features_type_id = [
        'PartDesign::Pad',
        'PartDesign::Revolution',
        'PartDesign::AdditivePipe',
        'PartDesign::AdditiveLoft',
        'PartDesign::AdditiveBox',
        'PartDesign::AdditiveCylinder',
        'PartDesign::AdditiveSphere',
        'PartDesign::AdditiveCone',
        'PartDesign::AdditiveTorus',
        'PartDesign::AdditivePrism',
        'PartDesign::AdditiveHelix'
        ]
    subtractive_features_type_id = [
        'PartDesign::Pocket',
        'PartDesign::Groove',
        'PartDesign::SubtractivePipe',
        'PartDesign::SubtractiveLoft',
        'PartDesign::SubtractiveBox',
        'PartDesign::SubtractiveCylinder',
        'PartDesign::SubtractiveSphere',
        'PartDesign::SubtractiveCone',
        'PartDesign::SubtractiveTorus',
        'PartDesign::SubtractivePrism',
        'PartDesign::SubtractiveHelix'
        ]
    for add_feature in body.Group:
        if add_feature.TypeId in additive_features_type_id:
            for sub_feature in body.Group:
                if sub_feature.TypeId in subtractive_features_type_id and  body.Group.index(add_feature) > body.Group.index(sub_feature):
                    return True
    return False

def has_additive_after_subtractive_all(doc: FreeCAD.Document):
    bodies = get_objects_by_type_id(doc, 'PartDesign::Body')
    for body in bodies:
        if has_additive_after_subtractive(body):
            return True
    return False

# ID 18: You have created a Part Design feature after a fillet or chamfer.

# ID 19: You have saved your FreeCAD document using a name that is not compatible with the Linux operating system.
# TODO: Requires 'pathvalidate' library, which is not included with the Python interpreter integrated in FreeCAD
def has_valid_filename():
    return NotImplementedError

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
    return NotImplementedError


def get_under_constrained_sketches(doc: FreeCAD.Document):
    """Returns all under-constrained sketches from the active FreeCAD document"""
    sketches = get_sketches(doc)
    under_constrained_sketches = []
    for sketch in sketches:
        if sketch.FullyConstrained == False and sketch.solve() == 0:
            under_constrained_sketches.append(sketch)
    return under_constrained_sketches
    

def get_over_constrained_sketches(doc: FreeCAD.Document):
    """Returns all over-constrained sketches from the active FreeCAD document"""
    sketches = get_sketches(doc)
    over_constrained_sketches = []
    for sketch in sketches:
        if sketch.FullyConstrained == True and sketch.solve() != 0:
            over_constrained_sketches.append(sketch)
    return over_constrained_sketches

def has_sketch_open_wire(sketch: Sketcher.Sketch):
    """Returns true if sketch contains an open wire"""
    wires = sketch.Shape.Wires
    for wire in wires:
        if wire.isClosed() == False:
            return True
    return False
        
def has_open_sketches(doc: FreeCAD.Document):
    """Returns true if document contains at least one sketch with an open wire"""
    sketches = get_sketches(doc)
    for sketch in sketches:
        if has_sketch_open_wire(sketch):
            return True
    return False

# TODO: Might not work as intended.
def doc_was_not_saved_recently(doc: FreeCAD.Document):
    """Checks how long ago the document was modified."""
    if doc.isSaved():
        return False
    date_string = doc.LastModifiedDate
    date_format = '%Y-%m-%dT%H:%M:%SZ'
    date_object = datetime.strptime(date_string, date_format)
    current_time = datetime.now()
    delta = current_time - date_object
    if delta.total_seconds() > 300:
        return True
    return False


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
        print("No object if given type found in the document")
        return
    return objects
    
def get_sketches(doc: FreeCAD.Document):
    """Returns all sketches from a FreeCAD document"""
    type_id = "Sketcher::SketchObject"
    sketches = []
    for obj in doc.Objects:
        if obj.TypeId == type_id:
             sketches.append(obj)
    return sketches

def get_rank(pts_reached, pts_available):
    ratio = pts_reached/pts_available
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
    screenshot_abs_path = FreeCADGui.activeDocument().activeView().saveImage("C:\\Users\\Aleksander\\Documents\\GitHub\\FreeCAD-Beginner-Assistant\\model_images\\test.png", 1543, 822, 'Transparent')
    print(screenshot_abs_path)
    
    """
    # Get the rank for this analysis
    rank = get_rank(pts_reached, pts_available)
    """

    result_dict = {
        "date" : str(today),
        "file" : filename,
        "screenshot" : "C:\\Users\\Aleksander\\Documents\\GitHub\\FreeCAD-Beginner-Assistant\\model_images\\test.png",
        "pts-reached" : "17",
        "pts-available" : "21",
        "rank" : "Bronze Apprentice",
        "best-practices" : []
    }

    result_dict["best-practices"].append(
        {
        "id" : 1,
        "action" : "You have referenced a face of your 3D model (topological element) for your sketch.",
        "effect" : "This might lead to the sketch losing its reference, when the topological elements change.",
        "solution" : "Reference one of the Origin planes or create a new plane, that also only references one of the Origin planes instead.",
        "status" : "Passed"
        }
    )

    result_dict["best-practices"].append(
        {
        "id" : 2,
        "action" : "You have created a sketch, that is under constrained",
        "effect" : "This might lead to unexpected behaviour, when you use that sketch for a feature",
        "solution" : "Go back to your sketch and fully define it using dimensional of geometrical constraints.",
        "status" : "Passed"
        }
    )

    result_dict["best-practices"].append(
        {
        "id" : 3,
        "action" : "You have created a sketch, that is over constrained",
        "effect" : "This might lead to unexpected behaviour, when you use that sketch for a feature",
        "solution" : "Go back to your sketch and remove redundant constraints.",
        "status" : "Passed"
        }
    )

    result_dict["best-practices"].append(
        {
        "id" : 4,
        "action" : "Your 3D model is not symmetric in relation to one of the Origin planes",
        "effect" : "Designing your 3D model symmetric to as many Origin planes as possible makes it easier to modify it in the future.",
        "solution" : "Try to create your 3D model symmetric in relation to as many Origin planes as possible.",
        "status" : "Passed"
        }
    )

    result_dict["best-practices"].append(
        {
        "id" : 5,
        "action" : "You have created a complex sketch that uses a lot of geometrical elements and constraints.",
        "effect" : "This might lead to performance issues and make building your 3D model slow.",
        "solution" : "Split up your complex sketch into multiple simple sketches if possible.",
        "status" : "Passed"
        }
    )

    return result_dict


