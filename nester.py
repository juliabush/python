"""This module is for nested lists in movies"""


def print_lol(the_list, indent=False, level=0, file=sys.stdout):
    """This is a recursive function for dealing with nested lists"""
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level + 1, file)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end="   ", file=file)
            print(each_item, file=file)
