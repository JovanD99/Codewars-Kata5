"""This regex expression ensures the password is at least 6 chars long, has at least one small, one big char and one digit"""

regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$"
