FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(f'{filepath}', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, in_filepath=FILEPATH):
    """ Write the to-do items list to the todos.txt file."""
    with open(f'{in_filepath}', 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello from the functions module!")
