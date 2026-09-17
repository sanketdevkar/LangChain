from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline;
llm = HuggingFacePipeline.from_model_id(
    model_id="meta-llama/Meta-Llama-3.1-8B-Instruct",
    task="text-generation" ,
    temperature=0.1,
    max_new_tokens=2,
)
model=ChatHuggingFace(llm=llm)
res=model.invoke("what is the capital of India")
print(res.content)