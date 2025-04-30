f=open('CdSe_CdZnS Core_Shell.txt','r')
# здесь первый столбик - длина волны, а второй - величина, которая от нее зависит
# код надо запустить в одной папке с этим файлом чтобы программа работала
s=f.readlines()
f.close()
v=[] #здесь хранятся значения величины
summ=0
amount=0
for line in s:
    line=line.replace('\n','')
    line = line.replace(',', '.')
    value=float(line.split('\t')[1])
    v.append(value)
    summ+=value
    amount += 1
average=summ/amount
average_deviation=0
average_square_deviation=0
for value in v:
    average_deviation+=(value-average)/amount
    average_square_deviation+=((value-average)**2)/amount
average_square_deviation=average_square_deviation**0.5
print("Cреднее отклонение: ",average_deviation, "\nСреднеквадратическое отклонение: ", average_square_deviation)
print("Cреднее значение: ",average) # если надо




