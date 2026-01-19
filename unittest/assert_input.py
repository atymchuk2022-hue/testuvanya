a = input("Enter a number: ")

assert a.isdigit(), "Input must be a number"

a = int(a)
assert a > 0, "Number must be greater than zero"

print(f"Entered number: {a}")
