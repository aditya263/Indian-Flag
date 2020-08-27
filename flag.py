from turtle import *                #we will import everything from turtle

speed(0)                            #speed of turtle i have given maximum
setup(800,500)                      #width,height of our screen window

penup()
goto(-400,250)                      #i will send my pen to corner and keep down there
pendown()


# now i will draw orangle rectangle
color("orange")
begin_fill()
forward(800)                        #as my screen width i have taken is 800 so i want to fill full my outout window
right(90)                           #turn 90 towards down
forward(167)                        #i will divide my screen in 3 parts orange, white , greem
right(90)
forward(800)
end_fill()
left(90)
forward(167)


#background is white so don't need to fill that again


#now green color
color("green")
begin_fill()
forward(167)                        
left(90)                           
forward(800)                       
left(90)
forward(167)
end_fill()



#now fill blue circle in middle of white frame
penup()
goto(70,0)
pendown()
color('navy')
begin_fill()
circle(70)                      #circle of radius 70
end_fill()


#its not hollow so make it hollow by adding white color inside blue circle of radius 60
penup()
goto(60,0)                  #radius we are taking 60 so choose cordinate accordingly
pendown()
color("white")
begin_fill()
circle(60)
end_fill()


#now we will add small circle on circumference of main circle
penup()
goto(-57,-8)
pendown()
color("navy")
for i in range(24):                 #there are 24 spokes in the ashok chakra so we will make small bumps by circle
    begin_fill()
    circle(3)                       #radius 3
    end_fill()
    penup()
    forward(15)
    right(15)
    pendown()



#now we will make small navy blue circle inside our white circle
penup()
goto(20,0)
pendown()
begin_fill()
circle(20)
end_fill()



#final part spokes in our flag
penup()
goto(0,0)
pendown()
pensize(2)
for i in range(24):
    forward(60)
    backward(60)
    left(15)


hideturtle()    
