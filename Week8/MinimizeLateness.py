# Python code to schedule jobs to minimize lateness
def minimize_lateness(jobs):
    # Step 1: sort the job based on deadlines
    jobs.sort(key=lambda x:x[1])
    # Declare variables:
    current_time = 0
    max_lateness = 0
    schedules = []
    
    # Step2: One pass through the jobs, process the finish time based on job duration. then compute the lateness
    for processing_time, deadline in jobs:
        start_time = current_time
        end_time = start_time + processing_time
        # Schedule the job at the current time
        schedules.append((start_time, end_time))
        
        # Calculate the lateness
        lateness = max(0, end_time-deadline)
        max_lateness = max(max_lateness, lateness)
        
        # Update the current time to the finish time of this job
        current_time = end_time
    return max_lateness, schedules

# List of jobs with (processing time, deadline)
jobs = [
    (3, 9),   # Job 1: Processing time 3, Deadline 9
    (2, 8),   # Job 2: Processing time 2, Deadline 8
    (1, 5),   # Job 3: Processing time 1, Deadline 5
    (4, 15)   # Job 4: Processing time 4, Deadline 15
]

max_lateness, schedule = minimize_lateness(jobs)

print("Max Lateness:", max_lateness)
print("Schedule:", schedule)