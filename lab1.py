#!/usr/bin/env python
# coding: utf-8

# In[1]:


import telegram
import requests

# Set up the bot
bot_token = '6000232164:AAHGCoI-iQhVXH8nEAAsvPh74igCeiFeXGc'
bot = telegram.Bot(token=bot_token)

# Define a function to handle incoming messages
def handle_message(update, context):
    # Get the search query from the user
    search_query = update.message.text
    
    # Make a request to your custom search API
    search_results = requests.get('https://customsearch.googleapis.com/customsearch/v1?key=AIzaSyB1ZiXYc7QLenBNz3YtFVwfp3_DW0HahEc&cx=8007119fe63c2435e',params={'q': search_query})
    
     # Parse the search results and get the top result
    search_results_json = search_results.json()
    if 'items' in search_results_json and len(search_results_json['items']) > 0:
        top_result = search_results_json['items'][0]
        
        # Send the top result back to the user
        chat_id = update.effective_chat.id
        bot.send_message(chat_id=chat_id, text=top_result['link'])
    else:
        # Send a message to the user indicating that no results were found
        chat_id = update.effective_chat.id
        bot.send_message(chat_id=chat_id, text="No results found for your search query")

# Set up the bot's message handler
from telegram.ext import MessageHandler, Filters, Updater

updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher
message_handler = MessageHandler(Filters.text & ~Filters.command, handle_message)
dispatcher.add_handler(message_handler)

# Start the bot
updater.start_polling()


# %%
