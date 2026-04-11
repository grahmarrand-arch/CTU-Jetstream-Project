import threading
import time
from queue import Queue

# ----------------------------
# "Database"
# ----------------------------
db = {}

# ----------------------------
# Search Index
# ----------------------------
search_index = {}

# ----------------------------
# Event Queue (CDC-style)
# ----------------------------
events = Queue()

# ----------------------------
# DB operations
# ----------------------------
def create_or_update_record(record_id, data):
    db[record_id] = data
    events.put(("upsert", record_id, data))  # emit event immediately

def delete_record(record_id):
    db.pop(record_id, None)
    events.put(("delete", record_id, None))

# ----------------------------
# Indexing logic
# ----------------------------
def index_record(record_id, data):
    # Simple full-text index (keyword-based)
    searchable_text = f"{data['title']} {data['description']}".lower()
    search_index[record_id] = searchable_text

def remove_from_index(record_id):
    search_index.pop(record_id, None)

# ----------------------------
# Event processor (real-time worker)
# ----------------------------
def event_worker():
    while True:
        event = events.get()
        if event is None:
            break

        action, record_id, data = event

        if action == "upsert":
            index_record(record_id, data)
            print(f"[INDEXED] {record_id}")

        elif action == "delete":
            remove_from_index(record_id)
            print(f"[DELETED FROM INDEX] {record_id}")

        events.task_done()

# ----------------------------
# Search function
# ----------------------------
def search(query):
    query = query.lower()
    results = []

    for record_id, text in search_index.items():
        if query in text:
            results.append((record_id, text))

    return results

# ----------------------------
# Start background indexing worker
# ----------------------------
worker_thread = threading.Thread(target=event_worker, daemon=True)
worker_thread.start()

# ----------------------------
# Demo
# ----------------------------
create_or_update_record(1, {
    "title": "Cheap Flights to NYC",
    "description": "Find affordable airline tickets"
})

create_or_update_record(2, {
    "title": "Hotel Deals Orlando",
    "description": "Best hotels near theme parks"
})

time.sleep(0.5)  # allow indexing

print("\nSearch results for 'hotel':")
print(search("hotel"))

# Update record → should propagate immediately
create_or_update_record(2, {
    "title": "Luxury Hotel Deals Orlando",
    "description": "5-star hotels near Disney World"
})

time.sleep(0.5)

print("\nSearch results after update:")
print(search("luxury"))

# Delete record → immediate removal
delete_record(1)

time.sleep(0.5)

print("\nSearch results after deletion:")
print(search("flight"))