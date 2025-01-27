from typing import Optional
import chainlit as cl

'''
@cl.password_auth_callback
def auth_callback(username: str, password: str):
    # Fetch the user matching username from your database
    # and compare the hashed password with the value stored in the database
    if (username, password) == ("sergio", "123"):
        return cl.User(
            identifier="sergio", metadata={"role": "admin", "provider": "credentials"}
        )
    else:
        return None
''' 

@cl.on_chat_start
async def on_chat_start():
    app_user = cl.user_session.get("user")
    await cl.Message(f"Ola Agente Comunitário").send()



@cl.step(type="tool")
async def marIA():
    # Fake tool
    await cl.sleep(2)
    return "Respondendo .... "


@cl.on_message  # this function will be called every time a user inputs a message in the UI
async def main(message: cl.Message):



    # Call the tool
    tool_res = await marIA()

    await cl.Message(content=tool_res).send()