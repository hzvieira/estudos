/*
Create a function that takes an integer as an argument 
and returns "Even" for even numbers or "Odd" for odd numbers.
*/

select 
  Case when 
    number % 2 = 0 
      then 'Even' 
      else 'Odd' 
  end as is_even 
from numbers