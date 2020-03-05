#c'etait plus simple pour nous d'ecrire les explications en anglais, en esperant que vous comprenez.

from turtle import* #when writing turtle cmds, don't have to write the 'turtle' part

l="F"
for a in range(0,13,1):    #0=starting point, 13=end point (computer can't run 2^3 2^4, 2^5..., 1= 1 by 1
     l=l.replace("F","+F--F+") #Lindenmayer system rule, + and - are constants, f is starting point, for every rule you get +f--f+
print(l)

home #putting in the middle of the canvas
down #put the pen down
speed(0) #fastest speed
for b in range(0,len(l)):
    if l[b]=="+":
        forward(0.3) #makes it viewable on laptop screen
        right(45)
    elif l[b]=="-":
        forward(0.3)
        left(45)

