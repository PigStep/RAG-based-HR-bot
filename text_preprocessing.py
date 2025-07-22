from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List, Dict
import re

file_path = "your_hr_document_example.txt" # your document in txt here

def load_text(file_path: str) -> str:
    """get text from document"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception as e:
        raise ValueError(f"File loading error: {str(e)}")

splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,          
        chunk_overlap=50
    )

all_splits = splitter.split_text(load_text(file_path))

print(f"All splits: {len(all_splits)}")
