
def is_isogram(string):
    string = string.lower()
    set_is=set(string)
    if len(set_is)==len(string):
        return True
    else:
        return False

