from langchain_openai import ChatOpenAI # Import the ChatOpenAI class to interact with OpenAI models
from dotenv import load_dotenv # Import load_dotenv to load environment variables from a .env file
from typing import TypedDict, Annotated, Optional, Literal # Import type hints for type annotations
from pydantic import BaseModel, Field # Import BaseModel and Field to create structured schemas

load_dotenv() # Load environment variables (e.g. OPENAI_API_KEY) into the environment

model = ChatOpenAI() # Initialize the ChatOpenAI model instance

# schema
class Review(BaseModel): # Define a Pydantic model to enforce the desired JSON schema for the output

    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list") # Require a list of strings representing key themes
    summary: str = Field(description="A brief summary of the review") # Require a string that summarizes the review
    sentiment: Literal["pos", "neg"] = Field(description="Return sentiment of the review either negative, positive or neutral") # Restrict sentiment output to "pos" or "neg"
    pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list") # Optional list of strings for the product pros
    cons: Optional[list[str]] = Field(default=None, description="Write down all the cons inside a list") # Optional list of strings for the product cons
    name: Optional[str] = Field(default=None, description="Write the name of the reviewer") # Optional string for the name of the reviewer
    

structured_model = model.with_structured_output(Review) # Bind the schema to the model so the output is coerced into a Review object

# Invoke the model with the raw text review, which will be parsed into the structured Review format
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

print(result) # Print the resulting structured Review object