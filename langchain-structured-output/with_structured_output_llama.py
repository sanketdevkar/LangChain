from dotenv import load_dotenv # Import load_dotenv to load environment variables
from typing import Optional, Literal # Import typing hints for optional fields and literal values
from pydantic import BaseModel, Field # Import BaseModel and Field for defining the schema
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint # Import HuggingFace integrations for LangChain

load_dotenv() # Load environment variables (like HuggingFace API tokens)

llm = HuggingFaceEndpoint( # Initialize a connection to a HuggingFace endpoint
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0", # Specify the model repository ID
    task="text-generation" # Specify the task type as text generation
)

model = ChatHuggingFace(llm=llm) # Wrap the endpoint in a ChatHuggingFace interface for chat-based interaction

# schema
class Review(BaseModel): # Define the Pydantic schema for the review output

    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list") # Require a list of key themes
    summary: str = Field(description="A brief summary of the review") # Require a summary string
    sentiment: Literal["pos", "neg"] = Field(description="Return sentiment of the review either negative, positive or neutral") # Restrict sentiment to pos or neg
    pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list") # Optional list of pros
    cons: Optional[list[str]] = Field(default=None, description="Write down all the cons inside a list") # Optional list of cons
    name: Optional[str] = Field(default=None, description="Write the name of the reviewer") # Optional reviewer name
    

structured_model = model.with_structured_output(Review) # Bind the Pydantic schema to the model to enforce structured output

# Invoke the model with the raw text review
result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Nitish Singh
""")

print(result) # Print the output which should match the Review schema