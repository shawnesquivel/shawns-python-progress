def test(expected, actual):
    if expected == actual:
        print("Test Passed")
    else:
        print("Test Failed")
    print(f"Expected: {expected} Actual: {actual}")


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

# Grab a subsection (defg)
# d = index 3
# g = index 6
print(letters[3:7])


# Step sizes
print(letters[::])

binary = "010101"

# go from beginnign to end in step sizes of 1
test("111", binary[1::2])
test("11", binary[1:4:2])

# Reversing a string
# Go from start to end, and use a negative step size
test("101010", binary[::-1])
