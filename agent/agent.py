import os
import json

from dotenv import load_dotenv
from google import genai
from google.genai import types


# --------------------------------------------------
# 1. Load API key
# --------------------------------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=api_key)


# --------------------------------------------------
# 2. Load private course data
# --------------------------------------------------

data_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "courses.json"
)

with open(data_path, "r") as file:
    courses = json.load(file)


# --------------------------------------------------
# 3. Define the TOOL
# --------------------------------------------------

def search_course(course_id):
    """
    Search the private course database using a course ID.
    """

    for course in courses:

        if course["course_id"].lower() == course_id.lower():

            return {
                "found": True,
                "course_id": course["course_id"],
                "course_name": course["course_name"],
                "fee": course["fee"],
                "duration": course["duration"]
            }

    return {
        "found": False,
        "message": "Course not found"
    }


# --------------------------------------------------
# 4. Tell the LLM about the available tool
# --------------------------------------------------

search_course_declaration = types.FunctionDeclaration(
    name="search_course",
    description="Search the private course database using a course ID.",
    parameters={
        "type": "OBJECT",
        "properties": {
            "course_id": {
                "type": "STRING",
                "description": "The course ID, for example AI202"
            }
        },
        "required": ["course_id"]
    }
)

tool = types.Tool(
    function_declarations=[search_course_declaration]
)


# --------------------------------------------------
# 5. AI AGENT LOOP
# --------------------------------------------------

print("=== AI Agent ===")
print("Type 'exit' to quit.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Agent: Goodbye!")
        break

    messages = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=user_input)
            ]
        )
    ]

    while True:

        # Ask the LLM what to do
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[tool]
            )
        )

        # Check whether the LLM wants to call a tool
        if response.function_calls:

            function_call = response.function_calls[0]

            print(
                f"[Agent Tool Call] "
                f"{function_call.name}({function_call.args})"
            )

            # Execute the selected tool
            if function_call.name == "search_course":

                result = search_course(
                    function_call.args["course_id"]
                )

                print(f"[Tool Result] {result}")

                # Add the model's response to the conversation
                messages.append(response.candidates[0].content)

                # Give the tool result back to the LLM
                messages.append(
    types.Content(
        role="user",
        parts=[
            types.Part.from_function_response(
                name=function_call.name,
                response=result
            )
        ]
    )
)

                # Continue the loop
                continue

        # No more tool calls → final answer
        print("Agent:", response.text)
        break