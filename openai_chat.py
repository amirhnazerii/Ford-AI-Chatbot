import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

def create_prompt(relevant_info, user_query):
    return f'''You are an expert in Ford vehicle specifications. Answer the question based on the relevant info below. 
    Info: {relevant_info}
    Question: {user_query}'''

COMPLETION_MODEL_NAME = "gpt-3.5-turbo-instruct"

def chatbot_response(prompt, max_prompt_tokens=1800, max_answer_tokens=100):
    try:
        response = openai.Completion.create(
            model=COMPLETION_MODEL_NAME,
            prompt=prompt,
            max_tokens=max_answer_tokens
        )
        return response["choices"][0]["text"].strip()
    except Exception as e:
        print(e)
        return ""
