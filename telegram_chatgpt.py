import os
import openai
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

openai.api_key = "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"

def handle_text(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    message = update.message.text

    # Call ChatGPT API to generate a response
    response = call_chatgpt(message)

    # Send the generated response back to the user
    context.bot.send_message(chat_id=chat_id, text=response)

# Try using other models as well like davincii turbo and all
def call_chatgpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
            )
    return response.choices[0].message['content']

def main():
    # Initialize your Telegram bot
    updater = Updater("5773770999:AAHj41SnM63CTPnjim399d6JJ1UznxP9YRg", workers=0)

    # Register the message handler
    updater.dispatcher.add_handler(MessageHandler(Filters.text, handle_text))

    # Start karo bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()