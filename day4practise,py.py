def operators_checker(a, b):
    print("Values:", "a =", a, ", b =", b)
    print("\n--- Arithmetic Operators ---")
    print("a + b =", a + b)
    print("a - b =", a - b)
    print("a * b =", a * b)
    print("a / b =", a / b if b != 0 else "Undefined (division by zero)")
    print("a % b =", a % b if b != 0 else "Undefined")
    print("a ** b =", a ** b)
    print("a // b =", a // b if b != 0 else "Undefined")

    print("\n--- Comparison Operators ---")
    print("a == b:", a == b)
    print("a != b:", a != b)
    print("a > b:", a > b)
    print("a < b:", a < b)
    print("a >= b:", a >= b)
    print("a <= b:", a <= b)

    print("\n--- Logical Operators ---")
    print("(a > 0 and b > 0):", a > 0 and b > 0)
    print("(a > 0 or b > 0):", a > 0 or b > 0)
    print("not(a > 0):", not(a > 0))

    print("\n--- Bitwise Operators ---")
    print("a & b =", a & b)
    print("a | b =", a | b)
    print("a ^ b =", a ^ b)
    print("~a =", ~a)
    print("a << 1 =", a << 1)
    print("a >> 1 =", a >> 1)

    print("\n--- Assignment Operators ---")
    x = a
    print("x = a ->", x)
    x += b
    print("x += b ->", x)
    x -= b
    print("x -= b ->", x)
    x *= b
    print("x *= b ->", x)
    if b != 0:
        x /= b
        print("x /= b ->", x)

    print("\n--- Membership Operators ---")
    lst = [a, b, 10]
    print("a in list:", a in lst)
    print("b not in list:", b not in lst)

    print("\n--- Identity Operators ---")
    print("a is b:", a is b)
    print("a is not b:", a is not b)


# 🔹 Take input from user
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

operators_checker(a, b)
