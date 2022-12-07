# Get the user's email address
email = input('Enter your email address?:').strip()

# Slice out the user name
user_name = email[:email.index('@')]

# Slice out the domain name
domain_name = email[email.index('@')+1:]

# Format massage
Format_ = (f"Your user name is {user_name} and your domain is {domain_name.upper()}")
# Display the result massage
print(format_)