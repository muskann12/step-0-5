

def greet(name: str):
    """
    This function greets the user by name.
    """
    print(f"Hello, {name}! Welcome to your UV project.")

def main():
    # Set your name here or get input from user
    user_name = "Muskan"
    
    # Calling the greet function
    greet(user_name)

if __name__ == "__main__":
    main()
