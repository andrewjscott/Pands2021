# Checks if there is a text file called count and if not creates it
# Author: Andrew Scott

with open("count.txt", "w") as f:
    data = "0"
    f.write(data)