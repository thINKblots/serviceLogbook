import json

LOG_FILE = "logbook.json"

try:
    with open(LOG_FILE, "r") as f:
        logbook = json.load(f)
    print("Logbook loaded successfully.")

except FileNotFoundError:
    print("No existing logbook found. Starting a new one.")
    logbook = []

while True:

    print("Service Logbook (CLI)")
    print("What do you want to do? ")
    print(" 1: Add new log")
    print(" 2: View all logs")
    print(" 3: Delete an entry")
    print(" 4: Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_machine = input("Enter Machine Details: ")
        add_issue = input("Describe Issue/Complaint: ")
        add_correction = input("Describe Work Performed: ")
        new_log_entry = {
            "machine": add_machine,
            "issue": add_issue,
            "correction": add_correction
        }
        logbook.append(new_log_entry)
        try:
            with open (LOG_FILE, "w") as f:
                json.dump(logbook, f, indent=4)
            print("\n***Log entry saved! ***\n")
        except Exception as e:
            print(f"\n***Error saving log: {e} ***\n")

    elif choice == "2":
        if not logbook:
            print("\nNo log entries found.\n")
        else:
            print("\n--- Viewing All Logs ---\n")
            for i, log in enumerate(logbook):
                print(f"    Entry#{i + 1}")
                print(f"    Machine:    {log['machine']}")
                print(f"    Issue:      {log['issue']}")
                print(f"    Correction: {log['correction']}")
                print(" -------------------------------")

    elif choice == "3":
        print("\n--- Delete an Entry ---")
        if not logbook:
            print("No log entries to delete.\n")
            continue # Goes back to the start of the 'while' loop

        # We can re-use the "View Logs" code to show the list first
        for i, log in enumerate(logbook):
            print(f"  Entry #{i + 1}: {log['machine']} ({log['issue']})")
        print("  --------------------")

        try:
            # Get user input for which entry to delete
            choice_to_delete = input("Enter the entry # you want to delete: ")
            
            # Convert the input to an integer
            index_to_delete = int(choice_to_delete) - 1 # -1 because lists start at 0
            
            # Check if the number is in a valid range
            if 0 <= index_to_delete < len(logbook):
                # Remove the item using .pop()
                removed_entry = logbook.pop(index_to_delete)
                print(f"\nSuccessfully deleted entry for: {removed_entry['machine']}")
                
                # --- CRITICAL: Save the file again! ---
                with open(LOG_FILE, "w") as f:
                    json.dump(logbook, f, indent=4)
                print("Logbook saved.\n")
                
            else:
                print("Invalid entry #. Please try again.\n")
                
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    
    elif choice == "4":
        print("Closing Logbook...")
        break

    else:
        print("\nInvalid choice, please try again.\n")
