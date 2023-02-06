import streamlit as st
import functions
import os

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


TODOS_PATH = "todos.txt"
if not os.path.exists(TODOS_PATH):
    with open(TODOS_PATH, "w"):
        pass

st.title("My Todo App")
st.subheader("Keeping Organized")
st.write("A simple way to manage a list from anywhere!")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter an item to-do...",
              on_change=add_todo,
              key="new_todo")


# st.session_state






