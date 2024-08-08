def main():
    try:
     a = int(input("Enter a number : "))
     print(a)
     return

    except Exception as e:
     print(e)
     return
    
        # it only use when we can use in a function also this return this finction
    finally:
        print("Inside Finally")  

main()


