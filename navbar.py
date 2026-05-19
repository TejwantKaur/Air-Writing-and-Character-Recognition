import streamlit as st


def navbar():
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Home", use_container_width=True):
            st.session_state.page = "Home"
            st.rerun()

    with col2:
        if st.button("Kids", use_container_width=True):
            st.session_state.page = "Kids"
            st.rerun()

    with col3:
        if st.button("TV", use_container_width=True):
            st.session_state.page = "TV"
            st.rerun()