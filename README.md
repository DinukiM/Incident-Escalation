
# Incident Management Script

This Python script helps monitor and manage incidents by tracking details such as severity, logged time, assigned team, and status. It also calculates the time elapsed since logging to enable time-based escalations based on severity.

## Features

- **Incident Tracking**: Logs incident details, including severity, team assignment, and status.
- **Time-Based Escalation**: Automatically calculates time differences to facilitate escalations based on severity levels (high, medium, low).

## Setup

### Prerequisites

- Python 3.x installed on your system.
- Clone this repository or download the `Incident.py` file to your project directory.

### Installation

To install necessary dependencies, if any are required (this script uses standard libraries), simply ensure you have Python 3 installed:

```bash
# Check if Python is installed
python3 --version
```

### Usage

1. **Running the Script**:
   To run the script and manage incidents, navigate to the directory containing `Incident.py` and execute the following command:

   ```bash
   Incident.py
   ```

2. **Integration into Existing System**:
   - Import functions from `Incident.py` into your main project script.
   - Use the incident list and escalation functions to manage incident records and escalate issues based on severity.

### Example

Here is a sample of code that shows you how to include the issue management features into your own script:

```python
from Incident import time_difference, incidents

# Check the time difference for a particular incident
incident_time = incidents[0]["time_logged"]
elapsed_time = time_difference(incident_time)
print(f"Time since logging: {elapsed_time} hours")
```

### Configuration

The script uses default escalation times based on incident severity:

- **High**: 2 hours
- **Medium**: 4 hours
- **Low**: 6 hours

You can adjust these times directly in the `escalation_times` dictionary within `Incident.py` as needed.


## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request with your proposed changes. All contributions are welcome!

---

### Author
Developed by Dinuki H. 

---
