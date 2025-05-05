
def get_input():
    n = int(input("\nEnter the length of the array: "))
    A1 = []
    for i in range(n):
        x = int(input(f"Enter element no. {i+1} of the array: "))
        A1.append(x)
    return A1

def display(A1):
    print("\nYour array is: [", end=" ")
    for i in range(len(A1)):
        if i < len(A1) - 1:
            print(A1[i], end=" , ")
        else:
            print(A1[i], end=" ")
    print("]\n\n")

def selection_sort(A1):
    n = len(A1)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if A1[j] < A1[min_index]:
                min_index = j
        
        if min_index != i:
            A1[min_index], A1[i] = A1[i], A1[min_index]
        
        #display(A1)

    print("Sorted Array: ")
    display(A1)

# Main program
A1 = get_input()
print("\n\nInitial Array: ")
display(A1)
selection_sort(A1)
