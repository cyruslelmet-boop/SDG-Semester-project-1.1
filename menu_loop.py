def main_menu():
    """
    Main controller loop for the Ushuru Wangu application.
    Keeps the application running until the user explicitly chooses to exit.
    """
    while True:
        # Display the clear menu system
        print("="*52)
        print(f" "*4, "USHURU WANGU-YOUR FUEL TRANSPARENCY TOOL")
        print("="*52)
        print("Welcome to Ushuru Wangu your fuel transparency tool,what would you like to do?")
        print("1.Calculate my fuel taxes")
        print("2.Report bad road condition")
        print("3.Exit Application")
        print("="*52)

        # Get user input and strip accidental spaces
        choice = input("Please select an option (1-3): ").strip()

        # Selection structures to handle choices
        if choice == "1":
            print("\n--- [Navigating to Tax Receipt Calculator] ---")
            # TODO: Call the tax calculator function here later

        elif choice == "2":
            print("\n--- [Navigating to Community Road Reporter] ---")
            # TODO: Call the road reporter function here later

        elif choice == "3":
            print("\nThank you for using Ushuru Wangu. Stand up for transparency!")
            break  # Exits the while loop, which terminates the program

        else:
            # Basic input validation to handle unexpected characters without crashing
            print("\n[ERROR] Invalid selection. Please type 1, 2, or 3.")

# This ensures the script runs automatically when executed
if __name__ == "__main__":
    main_menu()