# run_backend.py

import json
import firebase_config  # ensure Firebase is initialized
from data_structuring import structure_study_plan
from input_data import input_data
from progress_tracker import track_progress
from firebase_admin import db

# 1️⃣ Generate Study Plan
study_plan = structure_study_plan(input_data)

# 2️⃣ Example: completed topics (can later come from frontend)
completed_topics = ["Algebra"]

# 3️⃣ Track Progress
progress_summary = track_progress(study_plan, completed_topics)

# 4️⃣ Combine Data
output_data = {
    "student_id": input_data["student_id"],
    "student_name": input_data["student_name"],
    "study_plan": study_plan,
    "progress_summary": progress_summary
}

# 5️⃣ Export JSON
with open("student_study_data.json", "w") as f:
    json.dump(output_data, f, indent=4)
print("✅ JSON exported!")


# 7️⃣ Print Summary
print(f"Total Topics: {progress_summary['total_topics']}")
print(f"Completed Topics: {progress_summary['completed_topics_count']}")
print(f"Readiness: {progress_summary['readiness_percentage']}%")

print("✅ JSON exported!")
print("✅ Data uploaded to Firebase!")
print(f"Total Topics: {progress_summary['total_topics']}")

# Reference the parent node
ref = db.reference("/student_progress")
student_id = str(input_data['student_id'])

# Automatically create the child if missing
ref.child(student_id).set(output_data)
print("✅ Data uploaded to Firebase!")
