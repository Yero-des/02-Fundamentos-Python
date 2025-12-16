# Logic operators in Python
# and
age = 17
lincensed = False

if age >= 18 and lincensed:
  print("You can drive a car.")
elif age >= 18 and not lincensed:
  print("You need a license to drive a car.")
  
# or
is_student = False
membership = False

if is_student or membership:
  print("You get a discount.")
  
# not
is_admin = True

if not is_admin:
  print("Access denied. Admins only.")

# Short Circuiting
name = "yeromi zavala castillo"
print(name and name.capitalize())