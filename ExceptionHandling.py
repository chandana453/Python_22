#Exception Handling

#Try, Except and Finally


a=5
b=0

try:
    res=a/b  #keep the critical statements in try block
    print(res)


except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")

except Exception:
    print("Something went wrong!")

# except Exception as e:
#     print("cannot divide by zero",e)  # e returns the type of error(div by zero)

finally:
    print("Program executed")