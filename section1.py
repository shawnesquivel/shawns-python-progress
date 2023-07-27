# Section 3: Data Struture Objects / Basics
my_string = "Hello World"

get_the_o = my_string[-7]

print(get_the_o)

# indexing
letters = "abcdefghijk"

# only return c and onwards - everything from N and onwards
print(letters[2:])

# only return abcdefg - everything from the start until N+1
# g = index 6, so we should N+1 = 7... so we stop at 8 and include everything up to and not including 7
# in other words, go up to and DONT include 7 (H)
#
print(letters[:7])


# Practice one more time!
# Print h onwards
print(letters[7:])

# Print abcdefghij
print(letters[:10])
