import time
import threading
import queue

# Define a class to represent a data stream request
class DataStreamRequest:
    def __init__(self, stream_id, priority):
        self.stream_id = stream_id
        self.priority = priority
        self.timestamp = time.time()

    # Implement comparison methods to support priority-based sorting
    def __lt__(self, other):
        return self.priority < other.priority

# Define a function to process a data stream request
def process_request(request): 
    time.sleep(2)
    print(f"Processing request for Stream {request.stream_id} (Priority: {request.priority})")
    completed(request)

# Define a function to handle completed requests
def completed(request):
    completed_requests.append(request)

# Define a function to schedule data stream requests
def schedule_requests():
    while True:
        try:
            request = request_queue.get()  # Get the next request from the queue
            process_request(request)
            request_queue.task_done()
        except queue.Empty:
            break  # Exit the loop when there are no more requests

# Create a priority queue to hold data stream requests
request_queue = queue.PriorityQueue()

# Start a background thread for scheduling requests
scheduler_thread = threading.Thread(target=schedule_requests)
scheduler_thread.daemon = True
scheduler_thread.start()

# Get the number of streams from the user
while True:
    try:
        num_streams = int(input("Enter the number of streams: "))
        if num_streams <= 0:
            print("Please enter a positive integer.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

# Input data stream requests from the user and collect them in a list
user_requests = []
entered_values = set()  # Set to keep track of entered IDs and priorities

for i in range(num_streams):
    while True:
        try:
            stream_id = int(input(f"Enter Stream ID for Stream {i + 1}: "))
            priority = int(input(f"Enter Priority for Stream {i + 1} (<= {num_streams}): "))
            
            # Check if priority is within the valid range
            if priority <= 0 or priority > num_streams:
                print(f"Priority must be between 1 and {num_streams}.")
                continue
            
            # Check if the entered ID and priority combination is unique
            if (stream_id, priority) in entered_values:
                print("Stream ID and Priority combination already entered. Please enter unique values.")
                continue
            
            request = DataStreamRequest(stream_id, priority)
            user_requests.append(request)
            
            # Add the entered ID and priority to the set
            entered_values.add((stream_id, priority))
            
            break
        except ValueError:
            print("Invalid input. Please enter integers for Stream ID and Priority.")

# Add the user-entered requests to the priority queue
for request in user_requests:
    request_queue.put(request)

# Wait for all requests to be processed
request_queue.join()

# Display the "All requests processed" message
print("All requests processed.")

# Display completed requests along with IDs
completed_requests.sort(key=lambda x: x.stream_id)
for request in completed_requests:
    print(f"Completed request for Stream {request.stream_id} (Priority: {request.priority})")
