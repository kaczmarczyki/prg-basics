def f(name):
    split_name = name.split()
    acronym = ""
    for n in split_name:
        acronym += n[0]
    
    return acronym