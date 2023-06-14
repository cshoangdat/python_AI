def div(a,b):
    try:
        c = (a+b)/(a-b)
    # except ZeroDivisionError:
    #     print("Cannot divide with zero")
    #except:
    #   print(Cannot Excute)
    
    #Xac dinh chinh xac loi:
    except Exception as e:
        print(e)
    else:
        print(c)
    finally:
        print("This line always run!")

div(5,5)