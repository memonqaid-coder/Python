marks =float(input("Enter your marks: "))
if marks>90.99 and   marks<=100:
    print("Grade: A")
elif marks >= 71.99 and marks < 90.99:
    print("Grade: B")
elif marks >= 71.99:
    print("Grade: C")
elif marks >= 51.99 and marks < 71.99:
    print("Grade: D")
elif marks >= 35.99 and marks < 51.99:
    print("Grade: E")
elif marks < 35.99:
    print("Grade: F")
else:
    print("Invalid marks")

    