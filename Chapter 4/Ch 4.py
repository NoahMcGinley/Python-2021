def rectangle_pattern():
    
    rows = int(input("Enter the number of rows to print: "))
    columns = int(input('Enter the number of columns to print: '))
    print()
    
    for row in range(rows):
        for col in range(columns):
            print("*", end= '')
        print()

rectangle_pattern()