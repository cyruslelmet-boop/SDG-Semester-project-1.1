def add_pothole_report():
    """Collect a pothole report from the user and save it to a file."""
    print("\n=== REPORT A POTHOLE ===")

# Use a while loop to ensure location is not empty
    while True:
        location = input("Enter location: ").strip() # .strip() removes leading/trailing spaces
        if location == "":
            print("Location cannot be empty.")
            continue  # Restart the loop to ask again
        break #Exit the loop if location is valid

     # Use a while loop with try-except to handle non-numeric input
    while True:
        try:
            severity = int(input("Severity (1=small, 2=medium, 3=large): "))
            if severity < 1 or severity > 3:
                print("Must be 1-3.")
                continue # Restart loop for invalid range
            break  # Exit loop if input is valid (1-3)
        except ValueError: # This runs if the user enters something that's not a number
            print("Please enter a number.")

    desc = input("Brief description (optional): ").strip()
     # datetime.now() gets current date/time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # .strftime() formats it as "YYYY-MM-DD HH:MM:SS"
    # Start with timestamp, location, and severity
    report = f"{timestamp} | {location} | Severity {severity}"
    # Only add description if user provided one
    if desc:
        report += f" | {desc}" # Append description with separator
    # Add a newline character to separate reports in the file
    report += "\n"
    #Save to file
    try:
        # Open file in append mode ("a") - adds to end without overwriting
        # If file doesn't exist, it will be created automatically
        with open("pothole_reports.txt", "a") as f:
            f.write(report)  # Write the report string to file
        print("Report saved. Asante!")
    except Exception as e:
        # Catch any error (e.g., permission denied, disk full)
        print(f"Error saving report: {e}")
