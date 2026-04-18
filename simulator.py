import time

tickets = []

# Load tickets from file
def load_tickets():
    try:
        with open("tickets.txt", "r") as file:
            for line in file:
                parts = line.strip().split(" | ")
                ticket = {
                    "id": parts[0],
                    "issue": parts[1],
                    "priority": parts[2],
                    "status": parts[3]
                }
                tickets.append(ticket)
    except FileNotFoundError:
        print("No ticket file found, starting fresh.")

# Display tickets
def show_tickets():
    print("\n📋 Current Tickets:\n")
    for t in tickets:
        print(f"{t['id']} | {t['issue']} | {t['priority']} | {t['status']}")
    print()

# Create new ticket
def create_ticket():
    issue = input("Enter issue: ")
    priority = input("Enter priority (P1/P2/P3/P4): ")

    ticket_id = f"INC{len(tickets)+1:03d}"

    ticket = {
        "id": ticket_id,
        "issue": issue,
        "priority": priority,
        "status": "Open"
    }

    tickets.append(ticket)
    print(f"✅ Ticket {ticket_id} created successfully!")

# Update ticket status
def update_ticket():
    ticket_id = input("Enter Ticket ID: ")

    for t in tickets:
        if t["id"] == ticket_id:
            new_status = input("Enter new status (Open/In Progress/Closed): ")
            t["status"] = new_status
            print(f"✅ {ticket_id} updated!")
            return

    print("❌ Ticket not found.")

# Main menu
def main():
    load_tickets()

    while True:
        print("\n--- Incident Ticket Simulator ---")
        print("1. Show Tickets")
        print("2. Create Ticket")
        print("3. Update Ticket")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_tickets()
        elif choice == "2":
            create_ticket()
        elif choice == "3":
            update_ticket()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

        time.sleep(1)


if __name__ == "__main__":
    main()