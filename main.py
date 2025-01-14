import streamlit as st
from langchain_cohere import CohereEmbeddings
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_cohere.llms import Cohere
import os
from dotenv import load_dotenv

# Constants
CHROMA_PATH = "chroma"
PROMPT_TEMPLATE = """
Answer the question based on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

# Load environment variables
load_dotenv()
API_KEY = os.getenv('COHERE_API_KEY')

# Initialize Chroma and Model
db = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=CohereEmbeddings(cohere_api_key=API_KEY, model="embed-english-light-v3.0")
)
model = Cohere(temperature=0.75)

# Streamlit Interface
st.title("Survival Question Answering")
st.write("Ask a question related to survival, and get a response based on available context.")

# Text Input for Query
query = st.text_input("Enter your question here:")

if st.button("Search"):
    if query:
        # Perform similarity search and generate context
        references = db.similarity_search_with_score(query, k=3)
        context_text = "\n\n---\n\n".join([doc.page_content for doc, _ in references])

        # Create and format prompt
        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        prompt = prompt_template.format(context=context_text, question=query)

        # Generate response
        response_text = model.invoke(prompt)

        # Extract sources
        sources = [doc.metadata.get("id", "Unknown source") for doc, _ in references]

        # Display response in Streamlit
        st.subheader("Response")
        st.write(response_text)

        # Display sources
        st.subheader("Sources")
        for source in sources:
            st.write(f"- {source}")
    else:
        st.warning("Please enter a question.")
