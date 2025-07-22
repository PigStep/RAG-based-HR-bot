from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from text_preprocessing import all_splits

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2")

vectorstore =  Chroma(
    collection_name = "hr_docs",
    embedding_function=embedding_model,
    persist_directory="./chroma_db",
)

ids = vectorstore.add_texts(all_splits)
print(f"Persisted {len(ids)} to disk")