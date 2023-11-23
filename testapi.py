import openai

# Mock data for the purpose of the test
openai.api_key = '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'  # Replace with your actual API key for the test
messages = [
    {"role": "system", "content": "You are an experienced product manager and an expert in writing tickets."},
    {"role": "user", "content": "Write a brief bug report based on the following details: The app crashes when I try to upload a file."},
]

try:
    # Perform the OpenAI API call with the test data
    completion = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=messages
    )

    # Extract the message from the completion object
    message = completion.choices[0].get("message")
    if message:
        print(f"Generated ticket: {message}")
    else:
        print("No message was returned by the API.")

except openai.error.OpenAIError as openai_error:
    print(f"An error occurred with OpenAI: {openai_error}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")