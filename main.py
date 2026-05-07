from services.speaker_service import view_speakers_and_sessions
from services.attendee_service import view_attendees_by_company, add_new_attendee
from services.connection_service import view_connected_attendees, add_attendee_connection
from services.room_service import view_rooms


def show_menu():
    print("\nConference Management")
    print("=====================")
    print("MENU")
    print("====")
    print("1 - View Speakers & Sessions")
    print("2 - View Attendees by Company")
    print("3 - Add New Attendee")
    print("4 - View Connected Attendees")
    print("5 - Add Attendee Connection")
    print("6 - View Rooms")
    print("x - Exit application")


def main():
    while True:
        show_menu()

        choice = input("Choice: ").strip()

        if choice == "1":
            view_speakers_and_sessions()

        elif choice == "2":
            view_attendees_by_company()

        elif choice == "3":
            add_new_attendee()

        elif choice == "4":
            view_connected_attendees()

        elif choice == "5":
            add_attendee_connection()

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