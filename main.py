

def polishify(poland):
  sym_list = poland.split(' ')
  
  assert len(sym_list) == 3, "Неверное число операторов"
  assert sym_list[0] in ['+','-','*','/'] , "Данная операция не поддерживается"
  assert int(sym_list[1]) >=0 and int(sym_list[2]) >=0, "Введено отрицательное число"
  
  normal_line = (sym_list[1] + sym_list[0] + sym_list[2])
  try:
    result = eval(normal_line)
    print(result)
  except ZeroDivisionError:
    print('Вы попытались разделить на ноль. Ничего не вышло.')
  except NameError:
    print('Проверьте ваши числа. Возможно это совсем не числа')
  except Exception:
    print('Что-то пошло не так')

  except Exception as e:
    print(e)

polish = input('Введите ваше выражение в польской нотации: ')

polishify(polish)