
def main():
    Size = 0
    Arr = []    # already it is malloc

    print("Enter number of elements : ")
    Size = int(input())

    print("Enter the elements : ")

    Value = 0
    for i in range(Size):
        Value = int(input())
        Arr.append(Value)

    print(Arr)

main()

