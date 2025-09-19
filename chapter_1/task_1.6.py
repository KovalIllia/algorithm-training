num=int(input("Input int value: "))
answer=input("for byte: input 'b' OR for kilobyte: input 'k': ")
answer=answer.lower()
if answer=='b':
    print(f"{num} kilobyte = {num*1024} byte")
elif answer=='k':
    print(f"{num} byte = {num/1024} kilobyte")
else:
    print("Wrong input")