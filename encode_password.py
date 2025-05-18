import urllib.parse

password = "som@24"  # replace this with your actual password
encoded_password = urllib.parse.quote_plus(password)
print(encoded_password)
