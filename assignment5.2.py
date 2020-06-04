largest = None
smallest = None


def Maximum(largest, num):
    if largest is None:
        largest = num
    elif largest < num:
        largest = num
    return largest


def Minimum(smallest, num):
    if smallest is None:
        smallest = num
    elif smallest > num:
        smallest = num
    return smallest


while True:
    num = input("Enter a number: ")
    if num == "done":
        print("Maximum is ", largest)
        print("Minimum is ", smallest)
        break
    try:
        num = int(num)
        print(num)
        largest = Maximum(largest, num)
        smallest = Minimum(smallest, num)
    except:
        print('Invalid input')


