def generate_result_dict(fcstd_file_path=""):
    result_dict = {
        "date" : "01.01.2024",
        "file" : "test_file.FCStd",
        "screenshot" : "C:\\Users\\Aleksander\\Documents\\GitHub\\FreeCAD-Beginner-Assistant\\test_file.png",
        "pts-reached" : "14",
        "pts-available" : "21",
        "rank" : "bronze",
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

print(generate_result_dict())