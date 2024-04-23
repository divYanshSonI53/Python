# Friday, 12th April

weather = input("Provide weather: ")

if weather == "Sunny":
    activity = "Go for a walk" # આ example ની અંદર conditional if statement આપી છે કે અગર Sunny સાથે મેચ થાય તો એની અંદર જે નવું variable બનાવેલ છે activity નામ નું એમાં જે string આપેલ છે એ save થઈ જશે એવી જ રીતે બીજા example નીચે દર્શાવેલ છે જેમાં અગર weather ની અંદર જે input અપાશે એ અગર conditional if statement અને elif statement આપેલ છે એની સાથે match થઈ જશે તો activity variable ની અંદર એ જ save થસે ⬇️ 

elif weather == "Rainy":
    activity = "Read a Book"
elif weather == "Snowy":
    activity = "Build a Snowman"

print(activity)