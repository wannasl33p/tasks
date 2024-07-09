def get_fizz_buzz(n: int) -> list[int | str]:
    """
    If value divided by 3 - "Fizz",
       value divided by 5 - "Buzz",
       value divided by 15 - "FizzBuzz",
    else - value.
    :param n: size of sequence
    :return: list of values.
    """
    my_list : list[int | str] = []
    i=0
    while i<n :
      if i %3==0 :
         my_list.append('Fizz')
      elif i%5==0 :
         my_list.append('Buzz')
      elif i%15==0:
         my_list.append('FizzBuzz')
      else:
         my_list.append(i)
   
    return my_list
 
 
      
      
      
  
      