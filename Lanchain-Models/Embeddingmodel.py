from torch import embedding
from langchain_huggingface import HuggingFaceEmbeddings
embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
text="what is the capital of India"
#vector = embedding.embed_query(text)
#print(str(vector))  

doc=["Delhi is the capital of india",
    "Mumbai is the Financial capital of India",
    "kolkata is the Cultural capital of India"]
    
doc_vectors = embedding.embed_documents(doc)

print(str(doc_vectors))