from langchain_openai import ChatOpenAI # Import the ChatOpenAI class to interact with OpenAI models
from dotenv import load_dotenv # Import load_dotenv to load environment variables from a .env file
from typing import TypedDict, Annotated, Optional, Literal # Import typing helpers
from pydantic import BaseModel, Field # Import Pydantic tools

load_dotenv() # Load environment variables

model = ChatOpenAI() # Initialize the ChatOpenAI model instance

# schema
json_schema = { # Define a raw JSON schema dictionary to structure the output
  "title": "Review", # The title of the schema
  "type": "object", # The root type is an object (dictionary)
  "properties": { # Define the properties/fields of the object
    "key_themes": { # Field for key themes
      "type": "array", # It's an array (list)
      "items": { # The items in the array
        "type": "string" # Must be strings
      },
      "description": "Write down all the key themes discussed in the review in a list" # Description for the LLM
    },
    "summary": { # Field for summary
      "type": "string", # Must be a string
      "description": "A brief summary of the review" # Description for the LLM
    },
    "sentiment": { # Field for sentiment
      "type": "string", # Must be a string
      "enum": ["pos", "neg"], # Must be one of these exact values
      "description": "Return sentiment of the review either negative, positive or neutral" # Description for the LLM
    },
    "pros": { # Field for pros
      "type": ["array", "null"], # Can be an array or null
      "items": {
        "type": "string" # Array items must be strings
      },
      "description": "Write down all the pros inside a list"
    },
    "cons": { # Field for cons
      "type": ["array", "null"], # Can be an array or null
      "items": {
        "type": "string" # Array items must be strings
      },
      "description": "Write down all the cons inside a list"
    },
    "name": { # Field for name
      "type": ["string", "null"], # Can be a string or null
      "description": "Write the name of the reviewer"
    }
  },
  "required": ["key_themes", "summary", "sentiment"] # List of fields that the LLM must provide
}


structured_model = model.with_structured_output(json_schema) # Bind the raw JSON schema to the model to enforce structured output

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

print(result) # Print the resulting parsed JSON dictionary