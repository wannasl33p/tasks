def get_fizz_buzz(n: int) -> list[int | str]:
    """
    If value divided by 3 - "Fizz",
       value divided by 5 - "Buzz",
       value divided by 15 - "FizzBuzz",
    else - value.
    :param n: size of sequence
    :return: list of values.
    """
    my_list: list[int | str] = []
    for i in range(1,n):
      if i % 15 == 0:
         my_list.append('FizzBuzz')      
      elif i % 3 == 0:
         my_list.append('Fizz')
      elif i % 5 == 0:
         my_list.append('Buzz')
      else:
         my_list.append(i)
    return my_list
