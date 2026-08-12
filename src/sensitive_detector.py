import re

def detect_sensitive(message, message_id):

    text = str(message)

    patterns = {
        "one_time_password": r"\b\d{6}\b",
        "phone_number": r"\b\d{10}\b",
        "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "bank_account": r"\b\d{9,18}\b"
    }

    findings = []

    for sensitivity_type, pattern in patterns.items():

        matches = re.findall(pattern, text)

        if matches:

            masked = text

            for m in matches:
                masked = masked.replace(m, "*" * len(m))

            findings.append({
                "message_id": message_id,
                "sensitivity_type": sensitivity_type,
                "risk": "high",
                "masked_text": masked,
                "recommended_action": "do_not_store"
            })

    return findings