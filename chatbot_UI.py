import tkinter as tk
from tkinter import scrolledtext
import openai
from openai_chat import chatbot_response

# Initialize OpenAI API key
openai.api_key = "your_openai_api_key_here"

# Define function to handle user query and display response
def get_response():
    user_query = user_input.get("1.0", "end-1c")  # Get input from Text widget
    prompt = create_prompt(relevant_info="", user_query=user_query)  # Generate prompt
    response = chatbot_response(prompt)  # Get response from chatbot function

    # Display response in output box
    output_box.config(state="normal")  # Enable editing in output box
    output_box.delete("1.0", "end")  # Clear previous response
    output_box.insert("1.0", response)  # Insert new response
    output_box.config(state="disabled")  # Disable editing in output box

# UI setup
root = tk.Tk()
root.title("Ford Vehicle Specifications Chatbot")
root.geometry("600x400")

# Create prompt input box
tk.Label(root, text="Enter your question about Ford vehicle specifications:").pack(pady=10)
user_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=5)
user_input.pack(pady=10)

# Create output box for AI response
tk.Label(root, text="AI Assistant Response:").pack(pady=10)
output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=10, state="disabled")
output_box.pack(pady=10)

# Create submit button
submit_button = tk.Button(root, text="Get Response", command=get_response)
submit_button.pack(pady=20)

# Run the GUI application
root.mainloop()
