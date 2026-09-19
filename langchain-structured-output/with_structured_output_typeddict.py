from langchain_openai import ChatOpenAI # Import ChatOpenAI to interact with OpenAI models
from dotenv import load_dotenv # Import load_dotenv to load environment variables
from typing import TypedDict, Annotated, Optional, Literal # Import typing hints including TypedDict and Annotated

load_dotenv() # Load environment variables (e.g. OPENAI_API_KEY)

model = ChatOpenAI() # Initialize the ChatOpenAI model instance

# schema
class Review(TypedDict): # Define a TypedDict to specify the expected dictionary structure for the output

    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"] # Require a list of strings, with an Annotated description for the LLM
    summary: Annotated[str, "A brief summary of the review"] # Require a summary string, annotated with a description
    sentiment: Annotated[Literal["pos", "neg"], "Return sentiment of the review either negative, positive or neutral"] # Restrict sentiment to pos/neg with description
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"] # Optional list of pros with description
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"] # Optional list of cons with description
    name: Annotated[Optional[str], "Write the name of the reviewer"] # Optional string for the reviewer's name with description
    

structured_model = model.with_structured_output(Review) # Bind the TypedDict schema to the model so it returns a structured dictionary

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

print(result['name']) # Print just the 'name' field from the resulting dictionary