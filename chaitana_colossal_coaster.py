express_queue, normal_queue, ticket_type, person_name = ['Tony', 'Bruce'], ['RobotGuy', 'WW'], 0, 'HawkEye'

def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """Add a person to the 'express' or 'normal' queue depending on the ticket number.

    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue: list - names in the normal queue.
    :param ticket_type: int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    """

    if ticket_type == 0:
        normal_queue.append(person_name)
        return normal_queue
    elif ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    
# print(add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name))
# print(express_queue)
# print(person_name)
# express_queue = express_queue.append(person_name)
# print(express_queue)

queue = ["Natasha", "Steve", "Eltran", "Natasha", "Rocket"]

queue = ['Natasha', 'Steve', 'Ultron', 'Natasha', 'Rocket']

def remove_the_last_person(queue):
    """Remove the person in the last index from the queue and return their name.

    :param queue: list - names in the queue.
    :return: str - name that has been removed from the end of the queue.
    """

    # queue.remove(queue[-1])
    return queue[-1]

print(remove_the_last_person(queue))

# def sorted_names(queue):
#     """Sort the names in the queue in alphabetical order and return the result.

#     :param queue: list - names in the queue.
#     :return: list - copy of the queue in alphabetical order.
#     """

#     queue.sort()
#     return queue.copy()

# print(sorted_names(queue))