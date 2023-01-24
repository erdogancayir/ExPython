from os import strerror

# Initialize 26 counters for each Latin letter.
# Note: we've used comprehension to do that.
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
file_name = input("Enter the name of the file to analyze: ")
print(counters)
f = open(file_name, "rt")
try:
    for line in f:
        for char in line:
            if char.isalpha():
                counters[char.lower()] += 1
    f.close()
    for char in counters.keys():
        cnt = counters[char]
        if cnt > 0:
            print(char, '->',cnt)
except IOError as e:
        print("I/O error occurred: ", strerror(e.errno))