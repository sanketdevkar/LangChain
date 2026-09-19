"""
This script demonstrates using the StrOutputParser to chain multiple prompt-model
sequences together smoothly, automatically extracting string content from model outputs.
"""

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables (e.g., OpenAI API key)
load_dotenv()


# Initialize the OpenAI chat model (defaults to gpt-3.5-turbo or similar)
model = ChatOpenAI()

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

# Initialize the string output parser to easily extract text from the model's response
parser = StrOutputParser()

# Construct a single chain that generates a report, extracts the text, 
# feeds it into the summary prompt, generates the summary, and extracts the final text.
chain = template1 | model | parser | template2 | model | parser

# Execute the entire chain with the initial topic
result = chain.invoke({'topic': 'black hole'})

# Print the final parsed string (the summary)
print(result)
