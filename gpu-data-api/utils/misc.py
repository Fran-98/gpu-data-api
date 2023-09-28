import difflib

def get_closest_match(name:str, posibilities:list):
    print(posibilities)
    return difflib.get_close_matches(name, posibilities, 1, 0)[0]

