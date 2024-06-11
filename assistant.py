import FreeCAD # noqa


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


def get_under_constrained_sketches():
    """Check if FreeCAD document contains an under-constrained sketch"""
    sketches = get_sketches(FreeCAD.ActiveDocument)
    under_constrained_sketches = []
    for sketch in sketches:
        if sketch.FullyConstrained == False and sketch.solve(False) == 0:
            under_constrained_sketches.append(sketch)
    return under_constrained_sketches
    

def get_over_constrained_sketches():
    """Check if FreeCAD document contains an over-constrained sketch"""
    sketches = get_sketches(FreeCAD.ActiveDocument)
    over_constrained_sketches = []
    for sketch in sketches:
        if sketch.FullyConstrained == True and sketch.solve(False) != 0:
            over_constrained_sketches.append(sketch)
    return over_constrained_sketches

def get_sketches(doc):
    sketches = []
    for obj in doc.Objects:
        if obj: # check if object is sketch
             sketches.append(obj)
    return sketches

