


## Testing loops

def loops_test():
    numbers = [1,8,2,3]
    print_elems_for(numbers)
    # lists can handle different types
    numbers += [10,'aa']
    print_elems_while(numbers)

def print_elems_for(elements):
    result = ""
    for element in elements:
        result += str(element) + " "
    print(result)

def print_elems_while(elements):
    result = ""
    count = 0
    while(count < len(elements)):
        result += str(elements[count]) + " "
        count +=1
    print(result)

##

loops_test()