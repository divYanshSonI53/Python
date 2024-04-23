# Saturday, 13th April

# 10. Exponential Backoff
# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

# Real Life example  ⬇️

import time # time module

wait_time = 1   
max_retries = 5
attempts = 0

while attempts < max_retries: # આ line માં આપેલ છે કે attempts અગર max_retries થી ઓછા હશે તો જ loop ની અંદર અવાશે 

    print(f"Attempt {attempts + 1} - wait {wait_time}") # loop ની અંદર આવી ગયા પછી direct print statement આપે છે જેમાં લખ્યું છે કે {attempt + 1} એટલે કે ઉપર આપેલ જ છે કે attempts માં 0 છે તો એમાં 1 add થઈ જશે એવી જ રીતે wait_time આપેલ છે ઉપર 1 એમાં lopp જેટલી વાર ફરશે એટલી વાર 2 multiply થઈ જશે જેનું statement નીચે આપેલ છે 

    time.sleep(wait_time) # sleep method નો ઉપયોગ કર્યો છે 

    wait_time *= 2 # wait_time = wait_time * 2
    attempts += 1  # attempts = attempts + 1

