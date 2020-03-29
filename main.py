

def polishify(poland):
  sym_list = poland.split(' ')
  try:
    assert sym_list[0] in ['+','-','*','/'] , "Данная операция не поддерживается"
    assert len(sym_list) == 3, "Вы ввели неверное количество символов или не разделили их пробелом"
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