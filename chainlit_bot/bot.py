import chainlit as cl

@cl.on_message
def on_message(message: str):
    return f"Resposta para a mensagem: {message}"
