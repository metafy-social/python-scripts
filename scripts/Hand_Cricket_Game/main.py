import random

#Setting game parameters
Overs = int(input("Enter the number of Overs for the game : "))
Wkts = int(input("Enter the number of Wickets each side : "))
Balls = Overs*6
print("\n")

def Game_1() :

	Wkts_P1  = Wkts_P2  = Wkts
	Balls_P1 = Balls_P2 = Balls
	P2_score,P1_score = 0,0

	while(Wkts_P1 != 0 and Balls_P1 != 0) :
		P1_hand = int(input("Enter your hand : "))
		P2_hand = random.randint(1,6)
		print("Bot plays : ",P2_hand)

		if( P1_hand == P2_hand ):
			Wkts_P1 = Wkts_P1 - 1
			print("\nYou lost a wicket!!\n")

		else :
			P1_score += P1_hand

		Balls_P1 	= Balls_P1 - 1
		print("Balls left to play : ",Balls_P1,"\n")

	Target = P1_score + 1
	print("Bot's target is - ", Target, "\n")

	while( Wkts_P2 != 0 and Balls_P2 != 0 and P2_score<Target ) :
		P1_hand = int(input("Enter your hand : "))
		P2_hand = random.randint(1,6)
		print("Bot plays : ",P2_hand)

		if( P1_hand == P2_hand ):
			Wkts_P2 = Wkts_P2 - 1
			print("\nBot lost a wicket!!\n")

		else :
			P2_score += P2_hand

		Balls_P2 	= Balls_P2 - 1
		print("Balls left to play : ",Balls_P2)

	if( Wkts_P2 == 0 or P2_score <= Target ) :
		print("\nYou win the game !!!\n")

	elif( Wkts != 0 and P2_score>Target ) :
		print("\nBot wins the game !!!\n")




def Game_2() :

	Wkts_P1  = Wkts_P2  = Wkts
	Balls_P1 = Balls_P2 = Balls
	P2_score,P1_score = 0,0

	while(Wkts_P1 != 0 and Balls_P1 != 0) :

		P2_hand = int(input("Enter your hand : "))
		P1_hand = random.randint(1,6)
		print("Bot plays : ",P1_hand)
		
		if( P1_hand == P2_hand ):
			Wkts_P1 = Wkts_P1 - 1
			print("Bot loses a wicket!!\n")

		else :
			P1_score += P1_hand

		Balls_P1 	= Balls_P1 - 1
		print("Balls left to play : ",Balls_P1,"\n")

	Target = P1_score + 1
	print("Your target is - ", Target, "\n")

	while( Wkts_P2 != 0 and Balls_P2 != 0 and P2_score<Target ) :
		P2_hand = int(input("Enter your hand   : "))
		P1_hand = random.randint(1,6)
		print("Bot plays : ",P2_hand)

		if( P1_hand == P2_hand ):
			Wkts_P2 = Wkts_P2 - 1
			print("You lost a wicket!!\n")

		else :
			P2_score += P2_hand

		Balls_P2 	= Balls_P2 - 1
		print("Balls left to play : ",Balls_P2,"\n")

	if( Wkts_P2 == 0 or P2_score <= Target ) :
		print("\nBot wins the game !!!\n")

	elif( Wkts != 0 and P2_score>Target ) :
		print("\nYou win the game !!!\n")
		


#Toss
Toss_choice = input("You -> Enter H (Head) or T (Tails) : ")
Toss = random.choice(["H","T"])

if Toss_choice == Toss:
	print("You win the Toss.\n")
	P1 = input("Choose B(Batting) or F(Fielding) : ")
	print("You chose to " ,P1, "first.\n")

	if P1 == "B" :
		Game_1()
	else :
		Game_2()

else:
	print("Bot wins the Toss.\n")
	P2 = random.choice(["B","F"])
	print("Bot chose to " ,P2, "first.\n")

	if P2 == "B" :
		Game_2()
	else :
		Game_1()
