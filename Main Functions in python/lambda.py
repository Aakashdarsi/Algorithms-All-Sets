# lambda functions are the functions which are implicitly defined
# no need to define using the keyword def 
#Anonymous expressions are called as lambda expressions

full_name = lambda fn,ln: fn.strip().title()+" "+ln.strip().title()
print(full_name("aakash","darsi"))
help(full_name.sort())
