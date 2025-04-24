from collections import defaultdict
from threading import Lock

counter_data = defaultdict(lambda: {"count": 0, "initial": 0, "entered": 0, "exited": 0})
lock = Lock()

def update_counter(counter_id, count):
    with lock:
        counter_data[counter_id]["count"] = count

def update_tracker_stats(counter_id, initial, entered, exited):
    with lock:
        counter_data[counter_id]["initial"] = initial
        counter_data[counter_id]["entered"] = entered
        counter_data[counter_id]["exited"] = exited

def get_all_counters():
    with lock:
        return dict(counter_data)