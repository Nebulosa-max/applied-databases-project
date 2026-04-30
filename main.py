"""Main application file for the Applied Databases Project."""

from utils.menu import print_menu
from services.room_service import view_rooms


def main():
    """Run the main menu loop for the application."""
    while True:
        print_menu()
        choice = input("Choice: ").strip()

        if choice == "1":
            print("View Speakers & Sessions selected")

        elif choice == "2":
            print("View Attendees by Company selected")

        elif choice == "3":
            print("Add New Attendee selected")

        elif choice == "4":
            print("View Connected Attendees selected")

        elif choice == "5":
            print("Add Attendee Connection selected")

        elif choice == "6":
            view_rooms()

        elif choice.lower() == "x":
            print("Exiting application...")
            break

        else:
            print("Invalid choice. Please try again.")

        print()


if __name__ == "__main__":
    main()
