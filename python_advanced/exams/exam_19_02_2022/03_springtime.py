def start_spring(**kwargs):
    result = []
    spring_list = {}
    for spring_object, type in kwargs.items():
        if type not in spring_list:
            spring_list[type] = []

        spring_list[type].append(spring_object)

    sorted_elements = dict(sorted(spring_list.items(), key=lambda x: (-len(x[1]), x[0])))

    for type, spring_obj in sorted_elements.items():
        result.append(f"{type}:")
        for obj in sorted(spring_obj):
            result.append(f"-{obj}")

    return "\n".join(result)



# example_objects = {"Water Lilly": "flower",
#                    "Swifts": "bird",
#                    "Callery Pear": "tree",
#                    "Swallows": "bird",
#                    "Dahlia": "flower",
#                    "Tulip": "flower",}
# print(start_spring(**example_objects))
#
example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))

# example_objects = {"Magnolia": "tree",
#                    "Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Pear": "tree",
#                    "Cherries": "tree",
#                    "Shrikes": "bird",
#                    "Butterfly": "insect"}
# print(start_spring(**example_objects))