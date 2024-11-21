
# Umbra Database Login Simulation

# Predefined credentials (for demonstration purposes)
ADMIN_USERNAME = "UmbraAdmin"
ADMIN_PASSWORD = "A52t9"

def login():
    print("Welcome to the Umbra Database.")
    print("Please enter your credentials.\n")
    
    username = input("Username: ")
    password = input("Password: ")
    
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("\nAccess Granted. Welcome, Level 3 Clearance User.")
        print("Loading Umbra Database...")
        # Call a function to load further data or operations
        access_database()
    else:
        print("\nAccess Denied. Invalid credentials.")
        # Optionally, loop or exit based on retry logic
        retry = input("Would you like to try again? (yes/no): ").strip().lower()
        if retry == "yes":
            login()
        else:
            print("Exiting the system. Goodbye.")
            exit()

def access_database():
    print("\nUmbra Database System")
    print("Select an operation:")
    print("1. View Umbra Logs")
    print("2. Access Restricted Data")
    print("3. Exit")
    
    choice = input("Enter your selection: ")
    if choice == "1":
        print("\nDisplaying Umbra Logs...")
        # Add logic to show logs
    elif choice == "2":
        print("\nAccessing Restricted Data...")
        # Add logic for restricted data
    elif choice == "3":
        print("\nLogging out. Goodbye.")
        exit()
    else:
        print("\nInvalid choice. Returning to menu.")
        access_database()

# Start the login process
login()
