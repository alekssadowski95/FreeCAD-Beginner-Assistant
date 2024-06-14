import FreeCAD # noqa
import Sketcher # noqa


# From own testing:
# When sketches in FreeCAD are underconstrained, sketch.FullyConstrained returns False
# When sketches in FreeCAD are underconstrained, sketch.solve() returns 0
# When sketches in FreeCAD are overconstrained, sketch.FullyConstrained returns True
# When sketches in FreeCAD are overconstrained, sketch.solve() returns -2

""" From FreeCAD Documentation:

solve()

int SketchObject::solve( bool updateGeoAfterSolving = true	)
          	
solves the sketch and updates the geometry, but not all the dependent features (does not recompute) When a recompute is necessary, recompute triggers execute() which solves the sketch and updates all dependent features When a solve only is necessary (e.g.

DoF changed), solve() solves the sketch and updates the geometry (if updateGeoAfterSolving==true), but does not trigger any recompute.

Returns
    0 if no error, if error, the following codes in this order of priority: -4 if overconstrained, -3 if conflicting, -1 if solver error, -2 if redundant constraints 
"""


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

