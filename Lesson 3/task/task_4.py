from xml.etree import ElementTree as et


def build_tree(str):
    tree = et.fromstring(str)

    def add_elem(tree):
        dct = {"name": tree.tag, "children": []}
        for elem in tree:
            dct["children"].append(add_elem(elem))
        return dct

    def max_depth(tree):
        return 1 + max(map(max_depth, tree), default=-1)

    xml_tree = add_elem(tree)
    max_nest = max_depth(tree)
    return xml_tree, max_nest
