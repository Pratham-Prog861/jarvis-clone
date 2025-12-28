conversation_memory = []

def remember(role, content):
    conversation_memory.append({
        "role": role,
        "content": content
    })

def get_memory():
    return conversation_memory[-10:]
