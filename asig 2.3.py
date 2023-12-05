def is_even_num(input_list):
    even_num = []
    for num in input_list:
        if num % 2 == 0:
            even_num.append(num)
    return even_num

input = [1, 2 ,3 ,4 ,5 ,6 ,7, 8, 9, 10]
a = is_even_num(input)
print(a)