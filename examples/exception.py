try:
    def divison(n1,n2):
        # n1 = int(input("enter the no1\n"))
        # n2 = int(input("enter the no2\n"))
        div=n1/n2
        return(div)

    n1 = int(input("enter the no1\n"))
    n2 = int(input("enter the no2\n"))
    result=divison(n1,n2)
    # print(u)
except ValueError as ve:
    print(ve)
except ZeroDivisionError as zde:
    print(zde)
# except NameError:
#     print("name is not defined")
else:
    print(f'result is {result}')
finally:
    print("well done")


