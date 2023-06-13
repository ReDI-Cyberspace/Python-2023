from math import floor, ceil


list_numbers = [3.0,4.0,365.0,33.0,17.0, 8.0, 21.0, 23.0, 58.0]

def smallest_even(_list):
  _even_list = []
  _uneven_list = []
  for number in _list:
    if is_even(number): 
      _even_list.append(number)
    else:
      _uneven_list.append(number)
  _even_list.sort()
  _uneven_list.sort()

  print('Min even -> '+str(ceil(_even_list.first())))
  print('Min odd -> '+str(ceil(_uneven_list[0])))
  pass

def is_even(number):
  if number%2 == 0: return True
  else: return False

smallest_even(list_numbers)