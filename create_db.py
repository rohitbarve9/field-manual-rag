from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_cohere import CohereEmbeddings
from langchain_chroma import Chroma
import os
from dotenv import load_dotenv

CHROMA_PATH = "chroma"


def embed_and_save(chunks):
    load_dotenv()
    API_KEY = os.getenv('COHERE_API_KEY')
    BATCH_SIZE = 50
    db = Chroma(
        persist_directory=CHROMA_PATH, embedding_function=CohereEmbeddings(cohere_api_key=API_KEY, model="embed-english-light-v3.0")
    )

    chunks_with_ids = get_chunk_ids(chunks)
    existing_items = db.get(include=[]) 
    existing_ids = set(existing_items["ids"])
    new_chunks = []

    for chunk in chunks_with_ids:
        if chunk.metadata["id"] not in existing_ids:
            new_chunks.append(chunk)

    if len(new_chunks):
        for idx in range(0, len(new_chunks), BATCH_SIZE):
            chunk_subset = new_chunks[idx:idx+BATCH_SIZE]
            new_chunk_ids = [chunk.metadata["id"] for chunk in chunk_subset]
            db.add_documents(chunk_subset, ids=new_chunk_ids)


def get_chunk_ids(chunks):
    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"

        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        chunk_id = f"{current_page_id}:{current_chunk_index}"
        last_page_id = current_page_id
        chunk.metadata["id"] = chunk_id

    return chunks


def main():
    document_loader = PyPDFLoader("./data/field_service_manual.pdf")
    document = document_loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=10, length_function=len)
    chunks = splitter.split_documents(document)
    embed_and_save(chunks)
    

if __name__ == "__main__":
    main()


