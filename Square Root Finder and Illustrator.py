import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import time

#This is a two part script
#The first function does the actual logic
#Then the second function illustrates the first function's process of logic
def sqrroot():
    global seta, setb, setguess, guess, sqr, a, b
    sqr = float(input("What would you like to find the square root of?:   "))
    guess = sqr/10 #First guess for the sqr root. Im not using the math module because that's no fun and defeats the whole purpose of the program
    seta = []
    setb = []
    setguess = []
    while True:
        a = sqr/guess #Checker for square root
        b = (a+guess)/2 #Averages out guess and the radical divided by guess to converge
        seta.append(a) #Adds to a list for illustrations later.
        setb.append(b)
        setguess.append(guess)
        if round(guess, 5) == round(a, 5): #Square root checker
            return "The square root of {} is: {}!".format(str(round(sqr, 5)), str(round(guess, 5)))
        guess = b #If root not found, new guess is average a.k.a. 'b'.

print(sqrroot())
print(setguess)
print(seta)
print(setb)

# set up the figure
fig = plt.figure("Illustration of Babylonian Square Root Algorithm")
ax = fig.add_subplot(111)
ax.set_xlim(0,10)
ax.set_ylim(0,10)


# dimensions of lines
xmin = 0
xmax = 10
y = 5
height = 1


#Setting up the number line:
plt.hlines(y, xmin, xmax)
plt.vlines(xmin, y - height / 2., y + height / 2.)
plt.vlines(xmax, y - height / 2., y + height / 2.)
plt.text(xmin - 0.1, y, '0', horizontalalignment='right')
plt.text(xmax + 0.1, y, str(max(setguess)), horizontalalignment='left')
plt.pause(.01)

#Setting up the legend:
red_patch = mpatches.Patch(color='red', label='Average between guess and radicand÷guess')
yellow_patch = mpatches.Patch(color='yellow', label='New Guess')
blue_patch = mpatches.Patch(color='blue', label='Radicand÷Guess')
green_patch = mpatches.Patch(color='green', label='Correct Answer')
plt.legend(handles=[yellow_patch, blue_patch, red_patch, green_patch], loc='upper center')

#Plotting a point where all of the arrows stem from
plt.plot(5,y+2, 'ro', ms = 10, mfc = 'r') 


plt.axis('off')
fig.canvas.draw()
fig.canvas.flush_events()



guessindex = 0
time.sleep(7)

#Looping through the whole list of guesses to illustrate. 
for guessindex in range(0, len(setguess)-1):
        
    #Plotting the guess on the number line
    plt.plot((setguess[guessindex]/max(setguess))*10,y, 'ro', ms = 5, mfc = 'r')
    #Plotting the arrow on the number line
    plt.annotate('', ((setguess[guessindex]/max(setguess))*10,y), xytext = (5, y + 2), 
            arrowprops=dict(facecolor='yellow', shrink=0.01), 
            horizontalalignment='center')
    
    time.sleep(.5)
    fig.canvas.draw() #Update figure
    fig.canvas.flush_events() #Holds the figure until the next update is ready
    
    #Plotting the average between the guess and the radican/guess
    plt.plot((seta[guessindex]/max(setguess))*10,y, 'ro', ms = 5, mfc = 'r')
    #Plotting the arrow of the average between the guess and the radican/guess
    plt.annotate('', ((seta[guessindex]/max(setguess))*10,y), xytext = (5, y + 2), 
            arrowprops=dict(facecolor='blue', shrink=0.01), 
            horizontalalignment='center')
    
    time.sleep(.5)
    fig.canvas.draw()
    fig.canvas.flush_events()
    
    #Plotting the new guess (The new guess is just be the average from before so it diverges)
    plt.plot((setb[guessindex]/max(setguess))*10,y, 'ro', ms = 5, mfc = 'r')
    plt.annotate('', ((setb[guessindex]/max(setguess))*10,y), xytext = (5, y + 2), 
            arrowprops=dict(facecolor='red', shrink=0.01), 
            horizontalalignment='center')
    
    time.sleep(.5)
    fig.canvas.draw()
    fig.canvas.flush_events()
    
    #Do it until the lists are fully read through except for the answer
    #This line of code is for readability but it's not neccessary
    guessindex+=1
    
#After all of that plot the diverged answer with green!
guessindex=len(setguess)-1
time.sleep(2)

#Plot on number line of right answer
plt.plot((setb[guessindex]/max(setguess))*10,y, 'ro', ms = 5, mfc = 'r')
#Arrow for right answer
plt.annotate('', ((setb[guessindex]/max(setguess))*10,y), xytext = (5, y + 2), 
            arrowprops=dict(facecolor='green', shrink=0.01), 
            horizontalalignment='center')


plt.text(5, 10, "The square root of {} is: {}!".format(str(round(sqr, 5)), str(round(guess, 5))), horizontalalignment='center')

fig.canvas.draw()
fig.canvas.flush_events()

#Sleeping for 20 seconds so the tab auto closes after 20 seconds
time.sleep(20)