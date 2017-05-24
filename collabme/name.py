def full(person):
    full_name = ''

    if person.first_names:
        for name in person.rich_first_names:
            full_name += format(name) + ' '
    
    if person.middle_names:
        for name in person.rich_middle_names:
            full_name += format(name) + ' '
    
    if person.last_names:
        for name in person.rich_last_names:
            full_name += format(name) + ' '
    
    return full_name.rstrip()


def last(person):
    last_name = ''
    if person.last_names:
        for name in person.rich_last_names:
            last_name += format(name) + ' '
    return last_name.rstrip()

def sort_on_last(person):
    last_name = last(person)
    return last_name.lower()

def format(name):
    return name.render_as('text') 
