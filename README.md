# Project useful as python-fastapi-streamlit-langchain boilerplate
**TransactionManagement** is a robust Python-based application designed for the efficient management of banking transactions. This application not only facilitates seamless transaction processing but also offers a variety of reporting capabilities to help users gain insights from their data. Additionally, it incorporates an AI-powered chatbot to enhance user interaction and support.

## Features
- **Banking Transaction Management**: Streamline the process of recording, tracking, and managing banking transactions.
- **Report Generation**: Generate comprehensive reports with neumorous flexible filters available, based on transaction data, enabling users to analyze trends and make informed decisions.
- **AI Chatbot Integration**: Leverage an intelligent chatbot to assist users with queries, provide guidance, and improve overall user experience.
- **FastAPI Framework**: Built using FastAPI, ensuring high performance and easy scalability.
- **Streamlit Interface**: Utilize Streamlit for an intuitive and interactive web application interface that enhances user engagement.

##
**This is a very good production level boilerplate as well developed with fastapi, streamlit and langchain**
## Getting Started
To get started with the TransactionManagement app, follow these steps:
1. Clone this repository to your local machine and change your current directory to TransactionManagement directory.
    ```
    git clone https://github.com/YatharthAndharia/Boilerplate-Python-FastAPI-Streamlit-Langchain.git
    cd Boilerplate-Python-FastAPI-Streamlit-Langchain
    ```
## Run on local machine
2. Create a virtual environment and activate it.
    ```
    python -m venv venv
    source venv/bin/activate
    ```
3. Install all dependencies.
    ```
    pip install -r requirements.txt
    ```
4. Start the backend server.
    ```
    uvicorn app.main:app --reload
    ```
5. Run the frontend application.
    ```
    streamlit run streamlitapp/app.py
    ```

##
**This is still an underdevelopement project and stay connected for updates and new frameworks inclusion in boilerplate. I am also adding the dockerised version of this app soon.**