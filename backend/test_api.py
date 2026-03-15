#!/usr/bin/env python3
"""
Quick smoke-test for the MedNote API.
Run after starting the server:  python test_api.py
"""
import requests, json, sys

BASE = "http://localhost:8000"
USER_ID = "test_user_001"

def check(label, res, expected_status=200):
    ok = res.status_code == expected_status
    icon = "✅" if ok else "❌"
    print(f"{icon}  {label}  →  {res.status_code}")
    if not ok:
        print(f"   Body: {res.text[:200]}")
    return ok

passed = 0
failed = 0

# Health
r = requests.get(f"{BASE}/health")
if check("GET /health", r): passed += 1
else: failed += 1

# Create user
r = requests.post(f"{BASE}/api/user", json={"userId": USER_ID, "name": "Test User"})
if check("POST /api/user", r): passed += 1
else: failed += 1

# Sync data
payload = {
    "userId": USER_ID,
    "visits": [
        {"id": "v001", "doc": "Dr. Smith", "date": "Mar 15, 2025",
         "summary": "All good", "extractedItems": [], "meds": []}
    ],
    "reminders": [
        {"id": 1, "name": "Metformin", "dose": "500mg", "time": "8:00 AM",
         "done": False, "freq": "daily", "hr": 8, "mn": 0}
    ]
}
r = requests.post(f"{BASE}/api/sync", json=payload)
if check("POST /api/sync", r): passed += 1
else: failed += 1

# Pull records
r = requests.get(f"{BASE}/api/records/{USER_ID}")
if check("GET /api/records", r): passed += 1
else: failed += 1
data = r.json()
assert len(data["visits"]) == 1, "Expected 1 visit"
assert len(data["reminders"]) == 1, "Expected 1 reminder"
print(f"   visits={len(data['visits'])}, reminders={len(data['reminders'])}")

# Delete visit
r = requests.delete(f"{BASE}/api/visit/{USER_ID}/v001")
if check("DELETE /api/visit", r): passed += 1
else: failed += 1

print(f"\n{'─'*40}")
print(f"Results: {passed} passed, {failed} failed")
sys.exit(0 if failed == 0 else 1)
