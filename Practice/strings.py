st = "Sun rises in East ss"

# "ss tsaE ni sesir nuS"
print(st[::-1])

# "nuS sesir ni tsaE ss"


# "ss East in rises Sun"
print(" ".join(st.split(" ")[::-1]))

# ['Sun', 'rises', 'in', 'East', 'ss']
print(st.split(" "))