from datetime import datetime

data = datetime.now()
print('O tipo de dado inicial é: ', type(data))
data_em_texto = data.strftime('%d/%m/%Y %H:%M')
data = data_em_texto
print('O tipo de dado final é: ',type(data))
print('O conteúdo do dado é: ',data)
print('------------------------------')


date = datetime.strptime(data, '%d/%m/%Y %H:%M')


print(date, type(date))
