def main():
 import random  
 import getpass  
 from playsound import playsound  

 tips = []  
 tip_index = 0  
 lives = 5  

 category_names = {
    "animals": ["dino", "cat", "dog", "bird", "tiger", "lion", "cow", "elephant", "giraffe", "zebra", "snake", "monkey"],
    "cars": ["toyota", "lamborghini", "ferrari", "bmw", "ford", "mercedes", "audi", "tesla", "honda", "chevrolet", "jeep"],
    "sports": ["chess", "soccer", "basketball", "poker", "tennis", "volleyball", "boxing", "rugby", "cricket"],
    "countries": ["USA", "Canada", "Germany", "France", "Japan", "Morocco", "Brazil", "India", "Spain", "Egypt"],
    "fruits": ["apple", "banana", "orange", "grape", "pineapple", "kiwi", "mango", "pear", "peach", "watermelon"],
    "jobs": ["doctor", "engineer", "teacher", "scientist", "nurse", "pilot", "artist", "police", "firefighter", "chef"],
    "objects": ["phone", "pen", "laptop", "chair", "book", "mirror", "bottle", "scissors", "clock", "glasses"],
    "body parts": ["head", "hand", "foot", "leg", "eye", "elbow", "shoulder", "knee", "nose", "ear"],
    "foods": ["pizza", "burger", "pasta", "salad", "sushi", "taco", "steak", "noodles", "sandwich", "fries"],
    "video games": ["minecraft", "fortnite", "mario", "zelda", "pacman", "roblox", "valorant", "gta"]
 }

 category_tips = {
    "animals": {
        "dino": ["Extinct giant", "Lived millions of years ago", "Jurassic resident"],
        "cat": ["Loves naps", "Chases mice", "Purrs when happy"],
        "dog": ["Loyal friend", "Tail wagger", "Loves to fetch"],
        "bird": ["Has feathers", "Can fly", "Sings in the morning"],
        "tiger": ["Striped hunter", "Big cat", "Roars loudly"],
        "lion": ["King of jungle", "Has a mane", "Lives in pride"],
        "cow": ["Gives milk", "Moo sound", "Eats grass"],
        "elephant": ["Big ears", "Long memory", "Has a trunk"],
        "giraffe": ["Tallest animal", "Long neck", "Eats leaves"],
        "zebra": ["Black and white stripes", "Looks like a horse", "Found in Africa"],
        "snake": ["No legs", "Slithers", "Sometimes venomous"],
        "monkey": ["Loves bananas", "Climbs trees", "Playful animal"]
    },
    "cars": {
        "toyota": ["Reliable brand", "Popular in Japan", "Corolla maker"],
        "lamborghini": ["Very fast", "Luxury car", "Bull logo"],
        "ferrari": ["Italian", "Red racing beast", "Prancing horse logo"],
        "bmw": ["German maker", "Known for sporty feel", "Round blue-white logo"],
        "ford": ["American classic", "Model T origin", "Blue oval"],
        "mercedes": ["Luxury German car", "Three-pointed star", "Very elegant"],
        "audi": ["Four rings logo", "German engineering", "Makes the A4"],
        "tesla": ["Electric revolution", "Elon Musk's creation", "Silent and fast"],
        "honda": ["Reliable Japanese car", "Also makes bikes", "Civic model"],
        "chevrolet": ["American muscle", "Camaro and Corvette", "Bowtie logo"],
        "jeep": ["Off-road king", "Wrangler model", "Adventurer's ride"]
    },
    "sports": {
        "chess": ["Strategic board", "Kings and bishops", "Checkmate ends it"],
        "soccer": ["Global sport", "Round ball", "Goals and kicks"],
        "basketball": ["Orange ball", "Three-pointers", "Played on court"],
        "poker": ["Bluffing skill", "Full house wins", "Texas hold’em variant"],
        "tennis": ["Uses a racket", "Scored by love", "Grand Slam tournaments"],
        "volleyball": ["Spikes and blocks", "Played over a net", "Six players a team"],
        "boxing": ["Knockout possible", "Rounds and gloves", "In a ring"],
        "rugby": ["Oval ball", "Rough tackles", "Scrum formation"],
        "cricket": ["Bat and ball", "Wickets and overs", "Popular in India"]
    },
    "countries": {
        "USA": ["Stars and stripes", "50 states", "White House"],
        "Canada": ["Maple leaf", "Cold winters", "Bilingual nation"],
        "Germany": ["Berlin capital", "Oktoberfest", "Autobahn country"],
        "France": ["Eiffel Tower", "Croissants", "Paris city"],
        "Japan": ["Land of the Rising Sun", "Anime origin", "Tokyo city"],
        "Morocco": ["North Africa", "Couscous and tea", "Red flag with green star"],
        "Brazil": ["Amazon forest", "Carnival fest", "Soccer crazy"],
        "India": ["Taj Mahal", "Spices and colors", "Second most populated"],
        "Spain": ["Bullfights", "Flamenco dance", "Madrid capital"],
        "Egypt": ["Pyramids land", "Pharaohs", "Nile river flows here"]
    },
    "fruits": {
        "apple": ["Keeps doctor away", "Comes in red or green", "Can be a pie"],
        "banana": ["Yellow peel", "Monkeys love it", "Curved fruit"],
        "orange": ["Citrus fruit", "Rich in vitamin C", "Same name as its color"],
        "grape": ["Grows in bunches", "Can be made into wine", "Small and juicy"],
        "pineapple": ["Spiky outside", "Sweet and tropical", "Yellow inside"],
        "kiwi": ["Fuzzy skin", "Green inside", "Named after a bird"],
        "mango": ["King of fruits", "Juicy and sweet", "Tropical delicacy"],
        "pear": ["Bell-shaped", "Soft flesh", "Green or yellow"],
        "peach": ["Fuzzy skin", "Soft and juicy", "Used in cobbler"],
        "watermelon": ["Green outside", "Red inside", "Summer favorite"]
    },
    "jobs": {
        "doctor": ["White coat", "Saves lives", "Uses stethoscope"],
        "engineer": ["Builds systems", "Solves technical problems", "Often loves math"],
        "teacher": ["Explains things", "Gives homework", "Works in a classroom"],
        "scientist": ["Loves experiments", "Often in lab coat", "Discovers new things"],
        "nurse": ["Helps doctors", "Cares for patients", "Often in scrubs"],
        "pilot": ["Flies aircraft", "Wears uniform", "Sees the clouds"],
        "artist": ["Uses creativity", "Paints or draws", "Has a brush or pencil"],
        "police": ["Maintains order", "Wears a badge", "Drives a patrol car"],
        "firefighter": ["Fights flames", "Wears helmet", "Drives red truck"],
        "chef": ["Cooks food", "Wears hat", "Loves recipes"]
    },
    "objects": {
        "phone": ["Rings sometimes", "Used daily", "Now smart"],
        "pen": ["Writes ink", "Used on paper", "Has a cap"],
        "laptop": ["Portable screen", "Used for work", "Has a keyboard"],
        "chair": ["Sit on it", "Four legs usually", "Found in every home"],
        "book": ["Has pages", "Tells a story", "Read silently"],
        "mirror": ["Shows reflection", "Used in bathrooms", "Break it for bad luck"],
        "bottle": ["Holds liquid", "Twist the cap", "Can be plastic"],
        "scissors": ["Used for cutting", "Has blades", "Found in school bag"],
        "clock": ["Tells time", "Has hands", "Can tick"],
        "glasses": ["Help you see", "Worn on face", "Has lenses"]
    },
    "body parts": {
        "head": ["Top of body", "Holds brain", "Wears hat"],
        "hand": ["Has fingers", "Used to grab", "Shake with it"],
        "foot": ["Below leg", "Used for walking", "Wears shoes"],
        "leg": ["Helps run", "Below waist", "Has knee"],
        "eye": ["Helps see", "Has pupil", "Can blink"],
        "elbow": ["Arm joint", "Helps bend arm", "Often gets bumped"],
        "shoulder": ["Upper arm part", "Carries bag", "Can shrug"],
        "knee": ["Leg joint", "Helps in squats", "Can get scraped"],
        "nose": ["Smells things", "Above lips", "Can get stuffy"],
        "ear": ["Hears sound", "Has lobe", "Used for earrings"]
    },
    "foods": {
        "pizza": ["Cheesy triangle", "Often has toppings", "Italian origin"],
        "burger": ["Bun sandwich", "Has patty inside", "Fast food star"],
        "pasta": ["Italian dish", "Long or short", "Made of wheat"],
        "salad": ["Healthy choice", "Often has lettuce", "Eaten cold"],
        "sushi": ["Japanese roll", "Has rice and fish", "Served raw"],
        "taco": ["Mexican shell", "Filled with meat", "Crunchy or soft"],
        "steak": ["Meaty dish", "Served grilled", "Often medium or rare"],
        "noodles": ["Asian strings", "Served hot", "Can be ramen"],
        "sandwich": ["Bread pair", "Has filling", "Good for lunch"],
        "fries": ["Made from potato", "Golden sticks", "Served with burger"]
    },
    "video games": {
        "minecraft": ["Blocky world", "Build anything", "Watch out for Creepers"],
        "fortnite": ["Battle royale", "Dances included", "Build while fighting"],
        "mario": ["Jumps on mushrooms", "Saves princess", "Red hat hero"],
        "zelda": ["Link is hero", "Not the girl’s name", "Legendary adventure"],
        "pacman": ["Dots and ghosts", "Yellow eater", "Arcade classic"],
        "roblox": ["User-made games", "Avatars and scripts", "Huge platform"],
        "valorant": ["Tactical shooter", "Agents with powers", "5v5 battles"],
        "gta": ["Open-world crime", "Drive anything", "Wanted stars rise"]
    }
 }




 print(  
    "Select:\n"  
    " - Animals\n"  
    " - Cars\n"  
    " - video Games\n"  
    " - Countries\n"  
    " - Fruits\n"  
    " - Jobs\n"  
    " - Objects\n"  
    " - Body parts\n"  
    " - Foods \n "  
    " - Sports\n"
 )  

 category = input("What category: ").lower()  
 if category == "stop":  
    exit()  

 playsound(r"C:\Users\intel\Desktop\amjad\py\countdown1.wav")  
 print(category)  

# Example to access a specific tip from the selected category
 while category not in category_names:
       print (" chose from the list ! ")
       category = input("What category: ").lower()  
       if category == "stop":  
          exit()  
 item = random.choice(category_names[category])  # Randomly select an item from the chosen category
 tips = category_tips.get(category, {}).get(item, [])


          
# When user answers correctly:
 if tip_index < len(tips):
    print(f"💡 Tip: {tips[tip_index]}")
    tip_index += 1
 else:
    print("✅ No more tips, you're doing great!")




 revealed = ["*"] * len(item)
# revealed = ******
 print(revealed)
 lives = 5
 while lives > 0 and "*" in revealed:
   correct_guess = False
   guess = input(" guess a letter ")
   if guess == "hint":                                  #ihnt                         l;ll
       if tip_index < len(tips):
               print(f"💡 Tip: {tips[tip_index]}")
               tip_index += 1
               lives-= 1
               print (" you lost a life 💔")
               print ("ba9ilk " , lives , "lives ")
               playsound(r"C:\Users\intel\Desktop\amjad\py\tip.wav")
       else:
         print    ("NO MORE TIPS AVAILABLE")        
       playsound(r"C:\Users\intel\Desktop\amjad\py\tip.wav")



   for i in range(len(item)):
         if item[i] == guess :
             revealed[i] = guess                             
             print (revealed)
             correct_guess = True
             if tip_index < len(tips):
               print("💡 Tip:", tips[tip_index])
               tip_index += 1
             playsound(r"C:\Users\intel\Desktop\amjad\py\tip.wav")
             
         # here i want to add a tip every time correct answear
   if not correct_guess  and guess != "hint" :
          lives -= 1
          print (" you lost a life 💔")
          playsound(r"C:\Users\intel\Desktop\amjad\py\pop.wav")
       
 if input == "stop":      
   exit()            
 if "*" not in revealed:
            print ("                      ")
            print (" you win 😎😎 !")
            print ("                      ")
            if lives > 3 :
                  print (" You got :                     ")
                  print ("                      ")
                  print ("          ⭐⭐⭐       ")
                  print ("                      ")
            elif lives == 2 or lives == 3 :
                  print (" You got :                     ")
                  print ("                      ")
                  print ("         ⭐⭐       ")
                  print ("                      ")
            else :
                  print (" You got :                     ")
                  print ("                      ")
                  print ("         ⭐       ")
                  print ("                      ")
            playsound(r"C:\Users\intel\Desktop\amjad\py\completed level.wav")
 else : 
             print(" you lost 😥💔")
             playsound(r"C:\Users\intel\Desktop\amjad\py\lose.wav")
             print ("                                                     It was ," , item )
             print ("dumpy ! ")
             print ("                                                     TRY AGAIN !                   ")


 while True:
    user = input("Play again ? (yes/no) : ").lower()
    if user == "yes":
        print("                   NICEEE ! GOOD LUCK, CONCENTRATE ! 💪")
        main()
        break
    elif user == "no":
        print("                   Thanks for playing! Bye 👋")
        exit()
    else:
        print("                   ❌ Réponse non reconnue. Tape 'yes' ou 'no' !")
        # Et on redemande la question automatiquement
pass       
print("Welcome to the game!")
if __name__ == "__main__":
    main() 
