class UserAuthenticationSystem:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        if username in self.users:
            return False, "Username already exists"
        self.users[username] = password
        return True, "Registration successful"

    def login(self, username, password):
        if username not in self.users:
            return False, "User does not exist"
        if self.users[username] != password:
            return False, "Incorrect password"
        return True, "Login successful"

    def logout(self, username):
        if username not in self.users:
            return False, "User does not exist"
        return True, "Logout successful"


# Example usage
if __name__ == "__main__":
    authentication_system = UserAuthenticationSystem()

    # Register new user
    print(authentication_system.register_user("user1", "password1"))  # Output: (True, 'Registration successful')
    print(authentication_system.register_user("user2", "password2"))  # Output: (True, 'Registration successful')

    # Try to register user with existing username
    print(authentication_system.register_user("user1", "password3"))  # Output: (False, 'Username already exists')

    # Login with correct credentials
    print(authentication_system.login("user1", "password1"))  # Output: (True, 'Login successful')

    # Login with incorrect password
    print(authentication_system.login("user1", "wrong_password"))  # Output: (False, 'Incorrect password')

    # Logout user
    print(authentication_system.logout("user1"))  # Output: (True, 'Logout successful')
