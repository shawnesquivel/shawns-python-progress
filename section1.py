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


# 17. STRING PROPERTIES AND METHODS
# strings are immutable, you can't reassign parts of them

name = "shawn"
# below results in an error, since strings are objects that point to memory
# name[0] = "e" #error: string object doesn't support item reassignment

name = name + " esquivel"
print(name)

# print 300 z's
print("zzz" * 100)


# String Methods

# given a sentence, return the words only
sentence = "hello world it is a beautiful day my name is shawn"
all_words = sentence.split()
split_on_beautiful = sentence.split("beautiful")
print(all_words)
print(split_on_beautiful)


# format floating point numbers
unformatted = 123 / 4102
print(f"{unformatted}")

print(f"3 decimals: {unformatted:.3f}")

large_num = 1000000.12345
print(f"Large number with two decimals: {large_num:10.2f}")


""" LISTS """
part_one = [2, 10.2, "hello"]
part_two = ["world", 5]
# add
print(part_one[1:] + part_two)


# append
part_one.append("world")
print(part_one)

part_one.pop()
print(part_one)


numbers = [20, 19, 1, 29, 419, 22]
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)
