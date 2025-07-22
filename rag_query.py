from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from api_keys import LLM_API

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2")

vectorstore =  Chroma(
    collection_name = "hr_docs",
    embedding_function=embedding_model,
    persist_directory="./chroma_db",
)

promt = PromptTemplate.from_template(
    """You are a helpfull assistant to answer related to hr documents question on russian. 
    Use the following pieces of content to answer the question. 
    If you dont know answer say 'Пожалуйста, обратитесь к hr по поводу этого вопроса'
    Question: {question}
    Context: {context}
    Answer:"""
)

llm = ChatOpenAI(
    model="qwen/qwen3-235b-a22b-07-25:free",
    openai_api_key=LLM_API,
    openai_api_base="https://openrouter.ai/api/v1",
)

def ask_llm(question):

    retrieved_texts = vectorstore.similarity_search(question)
    doc_content = ' '.join([doc.page_content for doc in retrieved_texts])
    # print(doc_content)
    message = promt.invoke({"question":question, "context":retrieved_texts})
    answer = llm.invoke(message)
    return answer.content