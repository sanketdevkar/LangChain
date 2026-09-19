"""
This script demonstrates basic sequential calls to a language model without using
a formal output parser, instead relying on raw content attributes of the model's response.
"""

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

# Load environment variables (e.g., HuggingFace API token)
load_dotenv()

# Define the HuggingFace endpoint model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

# Initialize the ChatHuggingFace wrapper for the language model
model = ChatHuggingFace(llm=llm)

# 1st prompt -> template for generating a detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> template for generating a summary based on the provided text
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. \n {text}',
    input_variables=['text']
)

# Step 1: Format the first prompt with the chosen topic
prompt1 = template1.invoke({'topic': 'black hole'})

# Step 2: Invoke the model to generate the detailed report
result = model.invoke(prompt1)

# Step 3: Format the second prompt using the text content from the first result
prompt2 = template2.invoke({'text': result.content})

# Step 4: Invoke the model again to generate the summary
result1 = model.invoke(prompt2)

# Print the raw string content of the final summary
print(result1.content)

