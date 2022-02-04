#  SEcrets Module- As the numbers are reproducible in seed method it is not recommeded for the security purpose therefore secret module is is used
# They are used for password, security tokens or account authentication

# Disadvantage of Secret Module - It takes more time for these algorithm but it will generate a true random number

# Secrets module has 3 functions 
# 1 . randbelow
# 2 . randint - this will generate the random number between 0 to 4 in bits means  15 (1111)

import secrets

# It will print random numbers from 0 to 10, 10 is not included
a = secrets.randbelow(10)
print(a)

a = secrets.randbits(4)
# 4 is bits i.e it will return in 
print(a)


