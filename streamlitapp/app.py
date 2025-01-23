import streamlit as st

def main():
    st.set_page_config(
        page_title="HomeFinance",
        page_icon="🔁",
        layout="wide",
    )
    
    st.title("Transaction Manager")

    # Create columns for horizontal buttons with equal spacing
    # col1, col2, col3 = st.columns(3)

    # with col1:
    #     if st.button("Go to Page 1"):
    #         st.session_state["page"] = "page1"
    # with col2:
    #     if st.button("Go to Page 2"):
    #         st.session_state["page"] = "page2"
    # with col3:
    #     if st.button("Go to Page 3"):
    #         st.session_state["page"] = "page3"

    # Handle page redirection using session state
    if "page" in st.session_state:
        page = st.session_state["page"]
        if page == "page1":
            from streamlitapp.pages import Add_New_Account
            Add_New_Account.main()
        elif page == "page2":
            from streamlitapp.pages import All_Accounts
            All_Accounts.main()
        elif page == "page3":
            from streamlitapp.pages import Add_New_Transaction
            Add_New_Transaction.main()

if __name__ == "__main__":
    main()
