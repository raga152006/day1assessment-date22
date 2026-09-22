import json
import os

# Locate the private data file
data_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "courses.json"
)

# Load private course data
with open(data_path, "r") as file:
    courses = json.load(file)

print("=== Rule-Based Workflow ===")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Workflow: Goodbye!")
        break

    # Rule 1: Look for a known course ID
    course_id = None

    for course in courses:
        if course["course_id"].lower() in user_input.lower():
            course_id = course["course_id"]
            break

    # Rule 2: If course exists, return its fee
    if course_id:
        for course in courses:
            if course["course_id"] == course_id:
                print(
                    f"Workflow: The fee for {course['course_id']} "
                    f"is ₹{course['fee']}."
                )
                break
    else:
        print("Workflow: Course ID not found.")