# lambda function = function written in 1 line using lambda keyword
# accepts any number of arguments, but only has one expression.

# lambda parameters:expression

double = lambda x:x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name+" "+last_name
age_check = lambda age:True if age >= 19 else False

print(double(5))
print(multiply(5,5))
print(1,2,3)
print(full_name("Kiev","DevOps"))
print(age_check(18))
