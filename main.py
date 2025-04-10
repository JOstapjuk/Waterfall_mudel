import streamlit as st

if 'tasks' not in st.session_state:
    st.session_state.tasks = []

st.title("Todo list")

def add_task():
    task = st.text_input("Sisesta uus ülesanne:", key="new_task_input")
    if st.button("Lisa"):
        if task.strip():
            st.session_state.tasks.append({"text": task, "done": False})
            st.rerun()
        else:
            st.warning("Sisesta mitte tühi ülesanne")

add_task()

st.subheader("Ülesanne nimikiri:")

def show_task():
    if not st.session_state.tasks:
        st.info("Ei ole ülesandeid")
        return
    
    for index, task in enumerate(st.session_state.tasks):
        cols = st.columns([0.05, 0.90, 0.05])
        with cols[0]:
            task["done"] = st.checkbox("", value=task["done"], key=f"done_{index}")
        with cols[1]:
            if task["done"] == True:
                text = "------", task["text"],"-------"
            else:
                text = task["text"]
            st.markdown(text)
        with cols[2]:
            if st.button("Kustuta", key=f"delete_{index}"):
                st.session_state.tasks.pop(index)
                st.rerun()

show_task()
