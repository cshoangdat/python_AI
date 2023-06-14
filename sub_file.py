print(f"Sub file is {__name__}")

def nhap_ten():
    name = input("Name: ")
    print(f"Ten cua ban la: {name}")

def tuoi():
    age = int(input("Age: "))
    print(f"Tuoi cua ban la: {age}")

def main():
    nhap_ten()
    tuoi()
    
if(__name__ == "__main__"):
    main()