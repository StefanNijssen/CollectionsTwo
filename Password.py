import random
import string


characters1 = string.ascii_letters + string.digits + string.punctuation
password1 = ''.join(random.choice(characters1) for i in range(20))
characters2 = string.ascii_letters
password2 = ''.join(random.choice(characters2))
characters3 = string.ascii_letters + string.punctuation
password3 = ''.join(random.choice(characters3) for i in range(2))


print("Random password is:", password2 + password3 + password1 + password2)


