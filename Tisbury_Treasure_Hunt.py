x = ('Seaside Cottages', ('1', 'C'), 'blue')

# print(x[1][0] + x[1][1])

input_data =    (
                    ('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'), 
                    ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'), 
                    ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple')
                )

# (
#                 ('Scrimshawed Whale Tooth', '2A', 'Deserted Docks', ('2', 'A'), 'Blue'),
#                 ('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'),
#                 ('Robot Parrot', '1C', 'Seaside Cottages', ('1', 'C'), 'Blue'),
#                 ('Glass Starfish', '6D', 'Tangled Seaweed Patch', ('6', 'D'), 'Orange'),
#                 ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'),
#                 ('Pirate Flag', '7F', 'Windswept Hilltop (Island of Mystery)', ('7', 'F'), 'Orange'),
#                 ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple'),
#                 ('Model Ship in Large Bottle', '8A', 'Harbor Managers Office', ('8', 'A'), 'Purple'),
#                 ('Angry Monkey Figurine', '5B', 'Stormy Breakwater', ('5', 'B'), 'Purple'),
#                 ('Carved Wooden Elephant', '8C', 'Foggy Seacave', ('8', 'C'), 'Purple'),
#                 ('Amethyst  Octopus', '1F', 'Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow'),
#                 ('Antique Glass Fishnet Float', '3D', 'Spiky Rocks', ('3', 'D'), 'Yellow'),
#                 ('Silver Seahorse', '4E', 'Hidden Spring (Island of Mystery)', ('4', 'E'), 'Yellow')
#             )

def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """

    """
    ('Brass Spyglass', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')\n
    ('Vintage Pirate Hat', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange')\n
    ('Crystal Crab', 'Old Schooner', ('6', 'A'), 'Purple')\n
    """

    # result = """"""
    # for x in combined_record_group:
    #     result += f"(\'{x[0]}\', \'{x[2]}\', {x[3]}, \'{x[4]}\')\\n\n" 

    # return result

    # combined_records = tuple(tuple([i[0]])+i[2:] for i in combined_record_group)
    # report = "\n".join(str(record) for record in combined_records) + "\n"
    # return report

    combined_records = tuple(tuple([x[0]]) + x[2:] for x in combined_record_group)
    report = "\n".join(str(record) for record in combined_records) + "\n"
    return report

    # return combined_records

print(clean_up(input_data))

