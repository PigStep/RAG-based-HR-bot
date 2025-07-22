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

# def preprocess_text(text: str) -> str:
#     """Text preprocessing"""
#     text = re.sub(r'\n{3,}', '\n\n', text)
#     text = re.sub(r'(\d+\.\d+)', r'\n\1', text)
#     return text.strip()

# def split_with_recursive_splitter(text: str) -> List[Dict]:
#     """Splitting text"""
#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500,          
#         chunk_overlap=50,        
#         length_function=len,
#         separators=["\n\n", "\n", "(?<=\d\.\d)", " ", ""],  
#         keep_separator=True      
#     )
    
#     processed_text = preprocess_text(text)
    
#     # Creating chunks with meta
#     chunks = []
#     for i, chunk in enumerate(splitter.split_text(processed_text)):
#         section_match = re.search(r'^(\d+(?:\.\d+)*)', chunk)
#         section = section_match.group(1) if section_match else f"unk_{i}"
        
#         chunks.append({
#             "text": chunk,
#             "section": section,
#             "chunk_id": i,
#             "length": len(chunk)
#         })
    
#     return chunks

splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,          
        chunk_overlap=50
    )

all_splits = splitter.split_text(load_text(file_path))

print(f"All splits: {len(all_splits)}")
