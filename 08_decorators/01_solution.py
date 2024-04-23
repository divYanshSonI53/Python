# Thursday, 18th April

# Problem 1: Timing Function Execution
# Problem: Write a decorator that measures the time a function takes to execute.

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper 


@timer # આ line માં example_function નામ ના def પેલા જ @timer લખેલ છે timer એટલે કે timer નામ નું જે definition બનાવેલ છે અને એની આગડ @ decorator લગાડેલ છે એનો મતલબ એ છે કે example_function call કરાવવામાં આવશે ત્યારે એ timer નામ નું જે definition બનાવેલ છે એના through નિકડવું પડસે અને આ example_function નામ નું definition આખે આખું as a argument જાય છે timer નામ ના definition માં 

def example_function(n):
    time.sleep(n)

example_function(2)