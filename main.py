import sys
custom_path = "/path/to/your/files"
sys.path.append(custom_path)

import data_scraper
import RAG
import openai_chat
from data_scraper import flattener, load_urls_from_file
from RAG import generate_embeddings, create_faiss_index, query_table_data
from openai_chat import chatbot_response, create_prompt
import os


# URLs to scrape data from
# urls = data_scraper.load_urls_from_file(custom_path+"data/urls.csv")
urls = ["https://www.ford.com/suvs-crossovers/edge/models/edge-se/",
        "https://www.ford.com/suvs/explorer/2024/models/explorer-st/",
        "https://www.ford.com/suvs/mach-e/models/mach-e-select/",
        "https://www.ford.com/suvs/expedition/models/expedition-xl-stx/",
        "https://www.ford.com/cars/mustang/2024/models/gt-fastback/",
        "https://www.ford.com/suvs-crossovers/escape/2024/models/escape-st-line/",
        "https://www.ford.com/suvs/bronco-sport/models/bronco-sport-big-bend/",
        "https://www.ford.com/suvs/bronco/models/bronco-badlands/"]


class AI_chatbot():

    def __init__(self, urls, query):
        self.urls = urls
        self.query = query

    def get_web_data(self):
        # Scrape and parse HTML tables
        return flattener(self.urls)

    def get_rag_indices(self):
        # Generate embeddings
        embeddings = generate_embeddings(self.get_web_data())
        # create FAISS index
        return create_faiss_index(embeddings)

    def get_relevant_data(self):
        # Get retrieveal relevant data
        return query_table_data(self.query, self.get_rag_indices(), self.get_web_data())

    def generate_response(self, no_rag = True):
        # Generate response using OpenAI API

        prompt = create_prompt(self.get_relevant_data(), self.query)
        if no_rag:
            prompt = create_prompt("No extra information. asnwer based on your own knowledge", self.query)
        return chatbot_response(prompt)
    



"""
query = "Explain the engine of Ford Expedition 2024."
AI_chatbot_run = AI_chatbot(urls, query)
AI_chatbot_run.generate_response()
"""
