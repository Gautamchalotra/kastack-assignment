import re

def classify_message(message):
    text = str(message).lower()

    sensitive_keywords = [
        "password","otp","pin","cvv",
        "bank account","account number",
        "credit card","debit card",
        "upi","token"
    ]

    if any(k in text for k in sensitive_keywords):
        return {
            "category": "Sensitive Information",
            "confidence": 0.95,
            "reason": "Contains sensitive information."
        }

    personal_keywords = [
        "address",
        "phone",
        "mobile",
        "email",
        "passport",
        "aadhaar",
        "pan"
    ]

    if any(k in text for k in personal_keywords):
        return {
            "category": "Personal Information",
            "confidence": 0.90,
            "reason": "Contains personal details."
        }

    meeting_keywords = [
        "meeting",
        "event",
        "appointment",
        "schedule",
        "catch-up",
        "catch up",
        "reminder",
        "dinner",
        "webinar",
        "call"
    ]

    if any(k in text for k in meeting_keywords):
        return {
            "category": "Meeting or Event",
            "confidence": 0.92,
            "reason": "Contains meeting/event related information."
        }

    action_keywords = [
        "please",
        "review",
        "submit",
        "complete",
        "approve",
        "reply",
        "send",
        "update",
        "finish"
    ]

    if any(k in text for k in action_keywords):
        return {
            "category": "Action Required",
            "confidence": 0.90,
            "reason": "Requires user action."
        }

    promo_keywords = [
        "sale",
        "offer",
        "discount",
        "deal",
        "buy now",
        "limited time"
    ]

    if any(k in text for k in promo_keywords):
        return {
            "category": "Promotional",
            "confidence": 0.85,
            "reason": "Promotional content detected."
        }

    return {
        "category": "General Information",
        "confidence": 0.75,
        "reason": "No strong indicators found."
    }