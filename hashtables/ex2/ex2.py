#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(pile, length):
    table = {}
    route = []

    for ticket in pile: # O(n)
        table[ticket.source] = ticket.destination

    pointer = table['NONE']

    while pointer != 'NONE':
        route.append(pointer)
        pointer = table[pointer]

    route.append('NONE')

    return route
