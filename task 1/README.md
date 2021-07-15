import re

# Ввод символів
row=input("\nВведіть слова та числа: ")
# Виведення введених символів
print("\nВведені символи: ", row)


extract_letter="".join(re.split("[0-9]+", row))
extract_number="".join(re.split("[a-zA-Z]+", row))


extract_com_let=", ".join(extract_letter.split())
extract_com_num=", ".join(extract_number.split())

print("\nВведені слова: ", str(extract_com_let))


row_new_list=[]
for let in extract_letter.split():
    row_new_list.append(let[0].upper() + let[1:-1].lower() + let[-1].upper())
upper_let=" ".join(row_new_list)
print("\nВиведення слів з першими та останніми великими буквами: ", upper_let) 


max_num=""
numb_new_string=""

 
for numbers in extract_number:

    if "0" <= numbers <= "9":
    

        new_num_max=list(map(int, extract_number.split()))

# Виведення максимального значення
        max_num=max(new_num_max)


        numb_new_list=[]
        for element in new_num_max:
            if element != max_num:
                element=(element**new_num_max.index(element))
                numb_new_list.append(element)
            else:
                continue

        numb_new_string=", ".join([str(i) for i in numb_new_list])

# Виведення чисел
print("\nВсі числа: ", str(extract_com_num))
print("\nМаксимальне значення: ", max_num)
print("\nЧисла піднесені до кореня їх індексу: ", numb_new_string)

![task1](https://user-images.githubusercontent.com/86879264/125749605-3a4f073e-25a1-4d8e-ba23-28ecc99285fa.png)
