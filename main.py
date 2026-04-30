from utils.menu import print_menu


def main():
    while True:
        print_menu()
        choice = input("Choice: ").strip()

        if choice == "1":
            print("Option 1 selected")
        elif choice == "2":
            print("Option 2 selected")
        elif choice == "3":
            print("Option 3 selected")
        elif choice == "4":
            print("Option 4 selected")
        elif choice == "5":
            print("Option 5 selected")
        elif choice == "6":
            print("Option 6 selected")
        elif choice.lower() == "x":
            print("Exiting application...")
            break
        else:
            print("Invalid choice")

        print()

if __name__ == "__main__":
    main()