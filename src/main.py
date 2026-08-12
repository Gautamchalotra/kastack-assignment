import pandas as pd
import json

from classifier import classify_message
from extractor import extract_task_event
from sensitive_detector import detect_sensitive

df = pd.read_csv("data/messages.csv")

# =========================
# PART 1 CLASSIFICATION
# =========================

classification_results = []

for _, row in df.iterrows():

    result = classify_message(row["message"])

    classification_results.append({
        "message_id": row["message_id"],
        "category": result["category"],
        "confidence": result["confidence"],
        "reason": result["reason"]
    })

with open("outputs/classification_results.json", "w") as f:
    json.dump(classification_results, f, indent=4)

pd.DataFrame(classification_results).to_csv(
    "outputs/classification_results.csv",
    index=False
)

print("Classification Completed")

# =========================
# PART 2 TASK EXTRACTION
# =========================

task_results = []

for _, row in df.iterrows():

    task = extract_task_event(
        row["message"],
        row["message_id"]
    )

    if task:
        task_results.append(task)

with open("outputs/tasks_events.json", "w") as f:
    json.dump(task_results, f, indent=4)

pd.DataFrame(task_results).to_csv(
    "outputs/tasks_events.csv",
    index=False
)

print("Task Extraction Completed")

# =========================
# PART 3 SENSITIVE DATA
# =========================

sensitive_results = []

for _, row in df.iterrows():

    findings = detect_sensitive(
        row["message"],
        row["message_id"]
    )

    sensitive_results.extend(findings)

with open("outputs/sensitive_results.json", "w") as f:
    json.dump(sensitive_results, f, indent=4)

pd.DataFrame(sensitive_results).to_csv(
    "outputs/sensitive_results.csv",
    index=False
)

print("Sensitive Detection Completed")

print("\nSummary")
print("Messages:", len(df))
print("Classifications:", len(classification_results))
print("Tasks:", len(task_results))
print("Sensitive Findings:", len(sensitive_results))