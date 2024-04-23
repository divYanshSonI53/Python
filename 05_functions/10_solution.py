# Tuesday, 16th April

# 10. Recursive Function
# Problem: Create a recursive function to calculate the factorial of a number.

# હવે આ example માં આપડે recursive function એટલે કે definition બનાવાની છે તો કે recursive function હોય શું recursive function એટલે કે જે function પોતાને જ call કરે પોતાના જ function ની અંદર એને recursive function કેવાય જેનો example નીચે આપેલ છે ⬇️ 

def factorial(n):
    if n == 0: # આ line માં કીધેલ છે કે અગર n ની value 0 થઈ ગઈ છે તો બાર આવી જવાનું અને return કરી દેવાનું 1 કેમ કે 0 factorial ની value હોય 1 

        return 1
    
    else: # નઇ તો n ની જે value આવે એને n - 1 સાથે multiply કરતાં રહો જય સુધી value 0 ના થઈ જાય 

        return n * factorial(n - 1)
    

print(factorial(5))