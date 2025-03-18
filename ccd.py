import ipaddress
newfile = input("Введите название файла. Например ura_s_: ")
x, y = map(int, input("Введите диапазон чисел в названии файла через пробел. Например 13 22: ").split())
ip = ipaddress.ip_address(input('Введите ip адрес начала сети: '))
for i in range(x,y - 1):
    file_name = newfile +'{:04d}'.format(i)
    with open(file_name,'w') as f:
        f.write('ifconfig-push'+" "+str(ip + 2)+" "+str(ip + 1))
        ip += 4
