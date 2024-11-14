import time
from datetime import datetime

# Incident database (for demonstration, this could be a database or API in real systems)
incidents = [
    {"id": 1, "severity": "high", "time_logged": "2024-11-14 08:00", "assigned_team": "Team A", "status": "open"},
    {"id": 2, "severity": "medium", "time_logged": "2024-11-14 09:00", "assigned_team": "Team B", "status": "open"},
    {"id": 3, "severity": "low", "time_logged": "2024-11-14 10:00", "assigned_team": "Team C", "status": "open"}
]

# Define escalation time (in hours) for different severity levels
escalation_times = {
    "high": 2,   # escalate after 2 hours for high severity
    "medium": 4, # escalate after 4 hours for medium severity
    "low": 6     # escalate after 6 hours for low severity
}

# Function to calculate the time difference between incident log time and current time
def time_difference(log_time):
    log_time = datetime.strptime(log_time, "%Y-%m-%d %H:%M")
    current_time = datetime.now()
    return (current_time - log_time).total_seconds() / 3600  # returns time in hours

# Function to handle incident escalation
def escalate_incidents():
    for incident in incidents:
        # Calculate time elapsed since incident was logged
        elapsed_time = time_difference(incident["time_logged"])
        
        # Check if escalation is needed
        if elapsed_time >= escalation_times[incident["severity"]] and incident["status"] == "open":
            print(f"Escalating incident {incident['id']} (Severity: {incident['severity']}, Time Logged: {incident['time_logged']})")
            incident["status"] = "escalated"
            incident["assigned_team"] = "Escalation Team"
            print(f"Incident {incident['id']} has been escalated to the Escalation Team.\n")

# Run the escalation check
escalate_incidents()

