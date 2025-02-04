def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    # for i in args:
    #     for j in i:
    #         print(list(j))

    return list(args)

# print(get_list_of_wagons(1,5,2,7,4))

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    # first_id, second_id, id_1, *rest  = each_wagons_id
    first_id, second_id, *rest  = each_wagons_id
    # print(first_id, second_id)
    # print(missing_wagons)
    # print(rest)
    print([*missing_wagons, *rest, first_id, second_id])


"""
fix_list_of_wagons( [2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15])
                    [1, 3, 17, 6, 15, 7, 4, 12, 6, 3, 13, 2, 5]
"""

# fix_list_of_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15])
                # [1, 3, 17, 6, 15, 7, 4, 12, 6, 3, 13, 2, 5]

def add_missing_stops(a, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    print(a)
    print(kwargs.values())
    a.setdefault("stops", list(kwargs.values()))
    return a

# print(add_missing_stops({"from": "New York", "to": "Miami"},
#                         stop_1="Washington, DC", stop_2="Charlotte", stop_3="Atlanta",
#                         stop_4="Jacksonville", stop_5="Orlando"))
                        # {"from": "New York", "to": "Miami", "stops": ["Washington, DC", "Charlotte", "Atlanta", "Jacksonville", "Orlando"]}

def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    # print(zip(*wagons_rows))
    rest = zip(*wagons_rows)
    # print(a)
    return [list(t) for t in rest]

print(fix_wagon_depot([
                    [(2, "red"), (4, "red"), (8, "red")],
                    [(5, "blue"), (9, "blue"), (13,"blue")],
                    [(3, "orange"), (7, "orange"), (11, "orange")],
                ]))

                # [
                # [(2, "red"), (5, "blue"), (3, "orange")],
                # [(4, "red"), (9, "blue"), (7, "orange")],
                # [(8, "red"), (13,"blue"), (11, "orange")]
                # ]

                # [[(2, 'red'), (5, 'blue'), (3, 'orange')], 
                #  [(4, 'red'), (9, 'blue'), (7, 'orange')], 
                #  [(8, 'red'), (13, 'blue'), (11, 'orange')]]

