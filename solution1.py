import sys
#сумма цифр числа, введенего в командное окно
if __name__=="__main__":
    digit_string = sys.argv[1]

numbs = list()

for numb in digit_string:
    numbs.append(int(numb))

sum_numb = sum(numbs)
print(sum_numb)
