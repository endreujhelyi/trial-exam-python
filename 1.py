# Create a function that takes a list as a parameter,
# and returns a new list with all its element's values doubled.
# It should raise an error if the parameter is not a list.

def value_doubler(input_list):
    new_list = []
    if type(input_list) == list:
        new_list = [i * 2 for i in input_list]
        return new_list
    else:
        raise TypeError
