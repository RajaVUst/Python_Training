def is_even(n):
    if n % 2 == 0:
      print(f"{n} is even ")
    else:
       print(f"{n} is odd")
is_even(7)

# output
# 7 is odd

def is_even_ret(n):
   return n % 2 == 0

print(is_even_ret(2))

# output
# True