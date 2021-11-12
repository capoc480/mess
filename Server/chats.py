import database as db
from tinydb import Query

chats = db.chats

#first = chats.update("1")

Chat = Query()

def get_chat(chat_id = None):
    if chat_id == None:
        return None

    chat = chats.search(Chat.chat_id == chat_id)

    print(chat)

    if len(chat) == 0:
        return None

    return chat[0]

def get_chats_with_user(user_id):
    chat = chats.search((Chat.first == user_id) | (Chat.second == user_id))

    if len(chat) == 0:
        return None

    return chat[0]

def get_chat_with_users(first, second):
    chat = chats.search(((Chat.first == first) & (Chat.second == second)) | ((Chat.first == second) & (Chat.second == first)))

    if len(chat) == 0:
        return None

    return chat[0]

def count_chats():
    return len(chats.all())
    
def add_message_to_chat(first, second, data):
    chat = get_chat_with_users(first, second)
    
    if chat == None:
        return None
    
    messages = chat["messages"]
    
    count_messages = len(messages)
    
    data["message_id"] = count_messages + 1
    
    chat["messages"][count_messages + 1] = data
    
    ret = chats.update(chat, ((Chat.first == first) & (Chat.second == second)) | ((Chat.first == second) & (Chat.second == first)))
    
    return ret

def add_chat(first, second):
    chat = get_chat_with_users(first, second)

    if chat != None:
        return None

    chat_id = count_chats() + 1

    chats.insert({"first": first, "second": second, "messages": {}})

    chat = get_chat_with_users(first, second)

    if chat != None:
        return chat

    return None