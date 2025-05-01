import heapq

def max_tasks(tasks):
    # Sort tasks by deadline
    tasks.sort(key=lambda x: x['deadline'])

    total_time = 0
    min_heap = []  # to track durations of selected tasks
    completed_tasks = []

    for task in tasks:
        duration = task['duration']
        deadline = task['deadline']

        if total_time + duration <= deadline:
            heapq.heappush(min_heap, (-duration, task))  # use negative for max-heap behavior
            total_time += duration
        elif min_heap and -min_heap[0][0] > duration:
            # Replace longest duration task with this shorter one
            removed_duration, removed_task = heapq.heappop(min_heap)
            total_time += duration + removed_duration  # removed_duration is negative
            heapq.heappush(min_heap, (-duration, task))

    # Extract task names
    completed_tasks = [task['name'] for _, task in min_heap]
    return len(completed_tasks), completed_tasks

# Example input
tasks = [
    {'name': 'Task 1', 'deadline': 4, 'duration': 2},
    {'name': 'Task 2', 'deadline': 3, 'duration': 1},
    {'name': 'Task 3', 'deadline': 2, 'duration': 1},
    {'name': 'Task 4', 'deadline': 1, 'duration': 2},
]

# Run the function
count, selected = max_tasks(tasks)
print(f"Maximum tasks completed: {count}")
print("Tasks selected:", selected)
