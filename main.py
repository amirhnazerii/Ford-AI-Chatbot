from data_scraper import flattener
from RAG import generate_embeddings, create_faiss_index, query_table_data
from openai_chat import chatbot_response, create_prompt

# URLs to scrape data from
urls = [
    "https://www.ford.com/suvs-crossovers/edge/models/edge-se/",
    "https://www.ford.com/suvs/explorer/2024/models/explorer-st/",
    # Add more URLs as needed
]

# Step 1: Scrape and parse HTML tables
all_rows = flattener(urls)

# Step 2: Generate embeddings and create FAISS index
embeddings = generate_embeddings(all_rows)
index = create_faiss_index(embeddings)

# Step 3: Define query and retrieve relevant data
query = "Explain the engine of Ford Expedition 2024."
relevant_data = query_table_data(query, index, all_rows)

# Step 4: Generate response using OpenAI API
prompt = create_prompt(relevant_data, query)
response = chatbot_response(prompt)
print(response)
