#рисуем лестницу из решеток
#с выводом количества ступенек из командного окна
import sys

if __name__=="__main__":
    digit_string = sys.argv[1]

numb = int(digit_string)

for i in range(1,numb+1):
    print(' '*(numb-i)+'#'*i)
#for i in range(numb):
#    print(" " * (numb - i - 1), "#" * (i + 1), sep="")
