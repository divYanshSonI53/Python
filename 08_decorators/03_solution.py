# Friday, 19th April

# Problem 3: Cache Return Values
# Problem: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.

# import time

# def cache(func):
#     cache_value = {}
#     print(cache_value)
#     def wrapper(*args):
#         if args in cache_value:
#          return cache_value[args]
#         result = func(*args)
#         cache_value = result
#         return result
#     return wrapper


# @cache
# def long_running_function(a, b):
#     time.sleep(4)
#     return a + b


# long_running_function(2, 3)
# long_running_function(2, 3)

# This code defines a decorator cache that caches the results of a function call based on its arguments. The cache decorator defines a dictionary cache_value to store the cached results. The wrapper function checks if the arguments of the function call are already in the cache_value dictionary, and if so, returns the cached result. Otherwise, it calls the original function, stores the result in the cache_value dictionary, and returns the result.

# The long_running_function is then decorated with the cache decorator, which allows it to cache the results of its function calls. This function takes two arguments a and b, sleeps for 4 seconds, and returns the sum of a and b.

# Finally, the long_running_function is called twice with the same arguments (2, 3). The first time, the function runs for 4 seconds and returns the sum of 2 and 3, which is 5. The second time, the cached result is returned immediately without running the function again

# આ કોડ ડેકોરેટર કેશને વ્યાખ્યાયિત કરે છે જે તેની દલીલોના આધારે ફંક્શન કોલના પરિણામોને કેશ કરે છે. કેશ ડેકોરેટર કેશ્ડ પરિણામોને સંગ્રહિત કરવા માટે શબ્દકોશ cache_value વ્યાખ્યાયિત કરે છે. રેપર ફંક્શન તપાસે છે કે ફંક્શન કોલની દલીલો પહેલાથી જ cache_value શબ્દકોશમાં છે, અને જો એમ હોય તો, કેશ્ડ પરિણામ પરત કરે છે. નહિંતર, તે મૂળ કાર્યને કૉલ કરે છે, પરિણામને cache_value શબ્દકોશમાં સંગ્રહિત કરે છે અને પરિણામ પરત કરે છે.

# લાંબા_રનિંગ_ફંક્શનને પછી કેશ ડેકોરેટરથી શણગારવામાં આવે છે, જે તેને તેના ફંક્શન કૉલ્સના પરિણામોને કૅશ કરવાની મંજૂરી આપે છે. આ ફંક્શન બે દલીલો a અને b લે છે, 4 સેકન્ડ માટે ઊંઘે છે, અને a અને b નો સરવાળો આપે છે.

# છેલ્લે, લાંબા_રનિંગ_ફંક્શનને સમાન દલીલો (2, 3) સાથે બે વાર કહેવામાં આવે છે. પ્રથમ વખત, ફંક્શન 4 સેકન્ડ માટે ચાલે છે અને 2 અને 3 નો સરવાળો પરત કરે છે, જે 5 છે. બીજી વખત, કેશ્ડ પરિણામ ફંક્શનને ફરીથી ચલાવ્યા વિના તરત જ પરત કરવામાં આવે છે.


import time

def cache(func):
    cache_value = {}
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b

print(long_running_function(2, 3))
print(long_running_function(2, 3))