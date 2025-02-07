import openai
import asyncio
# Set your OpenAI API key
api_key = "sk-rpnwf3fSrEWsM-G1ndx_p6-FPHQonBTakc5ByKZfJBT3BlbkFJSwZ7O3ZHe8aEqaVcOeSB-E0XuHhZQWdw3CEINtqYMA"

# Define the prompt you want to send to the model
prompt = "Write a short story about a robot learning to play guitar."

from openai import AsyncOpenAI

client = AsyncOpenAI(api_key=api_key)
# async def f():
#     m=await client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
#     return m
# print(asyncio.run(f()))

import openai
import asyncio

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"

# Define the prompt you want to send to the model
prompt = "Write a short story about a robot learning to play guitar."

# Asynchronous function to get a response from GPT-3.5-turbo
async def get_gpt35_response(prompt):
    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,  # Adjust the max_tokens based on your needs
            temperature=0.7
        )

        # Extract the response content
        message = response['choices'][0]['message']['content']
        return message

    except Exception as e:
        return str(e)

# Main function to run the async call
async def main():
    response = await get_gpt35_response(prompt)
    print("Response from GPT-3.5-turbo:", response)

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())

