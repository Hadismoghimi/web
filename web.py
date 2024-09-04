import streamlit as st
import functions

def add_todo():
    todos = functions.get_todos()
    todo = st.session_state["new_todo"]+"\n"
    todos.append(todo)
    functions.set_todos(todos)
    st.session_state["new_todo"]=""


def remove_todo(todo):
    todos = functions.get_todos()
    todos.remove(todo)
    functions.set_todos(todos)
    st.rerun()

todos = functions.get_todos()

st.title("My Todo App")
st.header("Todo List")
st.write("Enter here your todo taks")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{todo}_{index}")
    if checkbox:
        remove_todo(todo)

st.text_input(label="",on_change=add_todo, placeholder="Enter your todo text", key="new_todo")

st.session_state



