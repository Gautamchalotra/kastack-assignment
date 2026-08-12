import re

def extract_task_event(message, message_id):

    text = str(message)

    date_match = re.search(r"\d{4}-\d{2}-\d{2}", text)
    time_match = re.search(r"\d{2}:\d{2}", text)

    date = date_match.group() if date_match else None
    time = time_match.group() if time_match else None

    keywords = [
        "meeting",
        "call",
        "appointment",
        "reminder",
        "event",
        "dinner",
        "catch-up",
        "review",
        "submit",
        "complete"
    ]

    if any(word in text.lower() for word in keywords):

        return {
            "item_id": f"TASK_{message_id}",
            "title": text[:60],
            "description": text,
            "date": date,
            "time": time,
            "person": None,
            "priority": "medium",
            "source_message_id": message_id
        }

    return None