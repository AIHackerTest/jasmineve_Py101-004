print("You enter a dark room with four doors. Which door do you go through?")
print("\tdoor1,\tdoor2,\tdoor3,\tdoor4")

door = input('> ')

if door == "1":
    print("There's a giant bear here eating a cheese cake. What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    
    bear = input("> ")
    
    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print("Well, doing %s is probably better. Bear runs away.") % bear
        
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    
    insanity = input("> ")
    
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello. Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck. GOod job!")
        
elif door == "3":
    print("Now you are in 'door 3', why do you choose this door?")
    print("1.\tfor fun 2.\tIt's none of your business 3.\tthree is my lucky number")
   
    reason = input("> ")
   
    if reason == "1":
        print("You are an awkward kiddo, now have some fun.")
        print("""You see a giant serpent wandering on the floor,
        and a beauty is standing if front of you. what do you do?""")
        print("option1: stand still")
        print("option2: lie down and play dead.")
        action = input("> ")
        if action == "1":
            print("Great! You are bitten by the serpent and now you are dead.")
        elif action == "2":
            print("Great! Now the beauty throws a knife at you and now you are dead.")
    
        
else:
    print("You stumble around and fall on a knife and die. Good job!")    
      
        
    