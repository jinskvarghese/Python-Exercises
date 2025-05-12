def pattern_fun(row_count):
    for i in range(1, row_count + 1):
        print((str(i) + ' ') * (row_count - i + 1))

row_count = int(input("Enter row count: "))
pattern_fun(row_count)