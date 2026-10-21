
import json
import os


class Complaint:
    def __init__(self, complaint_id, full_name, location,
                 complaint_type, description, status="Pending"):
        self.complaint_id = complaint_id
        self.full_name = full_name
        self.location = location
        self.complaint_type = complaint_type
        self.description = description
        self.status = status

        @classmethod
        def get_office_name(cls):
            return "Freetown Community Complaint Office"

    def display_complaint(self):
        print("\n--- Complaint Details ---")
        print("Complaint ID:", self.complaint_id)
        print("Full Name:", self.full_name)
        print("Location:", self.location)
        print("Complaint Type:", self.complaint_type)
        print("Description:", self.description)
        print("Status:", self.status)


class ComplaintManagementSystem:
    def __init__(self):
        self.office_name = "Freetown Community Complaint Office"
        self.complaints = []
        self.filename = "complaints.json"
        self.load_complaints()

    def load_complaints(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)

                for item in data:
                    complaint = Complaint(**item)
                    self.complaints.append(complaint)

            except (json.JSONDecodeError, TypeError):
                print("Warning: Could not read complaint records.")

    def save_complaints(self):
        data = []

        for complaint in self.complaints:
            data.append({
                "complaint_id": complaint.complaint_id,
                "full_name": complaint.full_name,
                "location": complaint.location,
                "complaint_type": complaint.complaint_type,
                "description": complaint.description,
                "status": complaint.status
            })

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def submit_complaint(self):
        print("\n--- Submit a Complaint ---")

        full_name = input("Enter your full name: ").strip()
        location = input("Enter your location: ").strip()
        complaint_type = input(
            "Enter complaint type (Roads, Water, Electricity, "
            "Garbage, Drainage, Other): "
        ).strip()
        description = input("Describe the problem: ").strip()

        if not all([full_name, location, complaint_type, description]):
            print("All fields are required.")
            return

        complaint_id = (
            max((c.complaint_id for c in self.complaints), default=1000)
            + 1
        )

        complaint = Complaint(
            complaint_id,
            full_name,
            location,
            complaint_type,
            description
        )

        self.complaints.append(complaint)
        self.save_complaints()

        print("\nComplaint submitted successfully!")
        print("Your Complaint ID is:", complaint_id)
        print("Your Status is: Pending")

    def view_all_complaints(self):
        if not self.complaints:
            print("\nNo complaints have been submitted yet.")
            return

        for complaint in self.complaints:
            complaint.display_complaint()

    def check_complaint_status(self):
        try:
            complaint_id = int(input("Enter Complaint ID: "))
        except ValueError:
            print("Please enter a valid number.")
            return

        for complaint in self.complaints:
            if complaint.complaint_id == complaint_id:
                print("Complaint ID:", complaint.complaint_id)
                print("Status:", complaint.status)
                return

        print("Complaint not found.")

    def update_complaint_status(self):
        try:
            complaint_id = int(input("Enter Complaint ID: "))
        except ValueError:
            print("Please enter a valid number.")
            return

        for complaint in self.complaints:
            if complaint.complaint_id == complaint_id:
                print("\n1. Pending")
                print("2. In Progress")
                print("3. Resolved")

                choice = input("Choose new status: ").strip()

                statuses = {
                    "1": "Pending",
                    "2": "In Progress",
                    "3": "Resolved"
                }

                if choice not in statuses:
                    print("Invalid status choice.")
                    return

                complaint.status = statuses[choice]
                self.save_complaints()

                print("Complaint status updated successfully!")
                return

        print("Complaint not found.")

    def run(self):
        while True:
            print("\n======================================")
            print(self.office_name.upper())
            print("======================================")
            print("1. Submit a Complaint")
            print("2. View All Complaints")
            print("3. Check Complaint Status")
            print("4. Update Complaint Status")
            print("5. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.submit_complaint()
            elif choice == "2":
                self.view_all_complaints()
            elif choice == "3":
                self.check_complaint_status()
            elif choice == "4":
                self.update_complaint_status()
            elif choice == "5":
                print("Thank you for using our system!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    system = ComplaintManagementSystem()
    system.run()
