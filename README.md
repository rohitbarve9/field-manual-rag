# Survival Support Bot
An AI-powered wilderness survival assistant with interactive guidance and reliable source citations.

## About
Survival Support Bot is a wilderness survival assistant powered by generative AI that provides real-time, context-aware guidance. It uses a Retrieval-Augmented Generation (RAG) approach with LangChain, ChromaDB, and Cohere embeddings to retrieve relevant information from multiple survival manuals and provide accurate, contextual advice. The bot, which is accessible through an interactive Streamlit web app with source citations, provides critical survival tips in an easy-to-use format and is hosted on the community cloud to ensure broad accessibility.

## Built With

<table>
  <tr>
    <td align="center">
      <a href="https://www.python.org">
        <img src="./images/python.jpg" width="50" height="60" alt="Python" />
      </a>
      <br>Python
    </td>
    <td align="center">
      <a href="https://cohere.com">
        <img src="./images/cohere.png" width="50" height="60" alt="Cohere" />
      </a>
      <br>Cohere Embeddings
    </td>
    <td align="center">
      <a href="https://www.langchain.com">
        <img src="./images/langchain.png" width="70" height="60" alt="Langchain" />
      </a>
      <br>Langchain
    </td>
    <td align="center">
      <a href="https://www.trychroma.com">
        <img src="./images/chromadb.png" width="70" height="60" alt="ChromaDB" />
      </a>
      <br>ChromaDB
    </td>
  </tr>
</table>



## Features
- **Contextual Retrieval**: Uses ChromaDB for efficient retrieval of relevant content from multiple survival manuals.
- **Generative Responses**: Employs Cohere embeddings and LangChain to generate natural, context-rich responses.
- **Interactive Web Application**: Built with Streamlit for user-friendly interaction and deployed on a community cloud.
- **Source Citations**: Displays citations for information sourced, ensuring transparency and reliability.

## Installation & Usage
1. Clone the repo:
   ```bash
   git clone https://github.com/rohitbarve9/field-manual-rag.git
2. Install dependencies
    ```bash
    pip install -r requirements.txt
3. Obtain your API key from the [Cohere website](https://dashboard.cohere.com/api-keys) and save the API key in the `.env` file in the following format:
    ```bash
    COHERE_API_KEY="YOUR_API_KEY"
4. Run the `create_db.py` file to create the ChromaDB vector database and populate it based on vectors derived from the documents in the `data` folder.
5. Run the `streamlit run main.py` to run the web application.


