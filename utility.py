def password_from_pid(pid):
    user = get_nex_account_by_pid(pid)

    if user is None:
        return "", "InvalidUsername"

    return user["password"], 0

def get_nex_account_by_pid(pid):
    # Dummy function to simulate fetching user data
    # Replace this with actual database query logic
    if pid == 12345:
        return {"password": "example_password"}
    return None

# Example usage
pid = 12345
password, error_code = password_from_pid(pid)
print(f"Password: {password}, Error Code: {error_code}")
