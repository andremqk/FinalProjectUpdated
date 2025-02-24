import random

#ROULETTE
# defining the red numbers of the roulette (0 is green)
red_numbers = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}


def menu_casino():
    '''
    main function that is the menu of the casino and lets the user choose what he's going to play
    :return: nothing
    '''
    while True: #means that the code/game will repeat until the user breaks
        print("Welcome to the Mini Casino!")
        print("1. Play Roulette")
        print("2. Play Blackjack")
        print("0. Exit the casino")
        choice = input("Enter your choice: ").strip() #the strip() is used to correct possible spaces

        if choice == "1":
            roulette_game()
        elif choice == "2":
            blackjack_game()
        elif choice == "0":
            print("Thanks for coming! Goodbye.")
            break #takes the player out of the game if he presses 0
        else:
            print("Invalid option. Please choose an valid option.")


def roulette_game():
    '''
    roulette game where user can bet in a number or a color
    it randomizes and gives a number and color
    :return: the number and color and the results
    '''
    print("\n--- Roulette ---")
    print("Bet Options:")
    print("1. Bet on a specific number (0-36)")
    print("2. Bet on a color (red or black)")

    bet_type = input("Choose your bet type (1 or 2): ").strip()

    if bet_type == "1":
        #bet on a number
        try:
            user_number = int(input("Enter the number you want to bet on (0-36): ").strip())
            if user_number < 0 or user_number > 36:
                print("Number must be between 0 and 36!")
                return
        except ValueError:
            print("Invalid input. Please enter an integer between 0 and 36.")
            return
    elif bet_type == "2":
        #bet on a color
        user_color = input("Enter the color you want to bet on (red or black): ").strip().lower()
        if user_color not in {"red", "black"}:
            print("Invalid color. Please choose either 'red' or 'black'.")
            return
    else:
        print("Invalid bet type selected.")
        return

    #spins the roulette and gives a number and its respective color
    result_number = random.randint(0, 36)
    if result_number == 0:
        result_color = "green"
    elif result_number in red_numbers: #if the number is in the list we defined in the beginning as red_numbers is red
        result_color = "red"
    else:
        result_color = "black"

    print(f"\nThe roulette wheel spins and lands on {result_number} ({result_color})!")

    #results
    if bet_type == "1": #if he chooses to bet in a number
        if result_number == user_number:
            print("Congratulations! Your number hit. You win!")
        else:
            print("Sorry, your number did not hit. Better luck next time!")
    else: #if he chooses to bet in a color
        if result_color == user_color:
            print("Congratulations! The color matches. You win!")
        else:
            print("Sorry, the color doesn't match. You lose.")

#BLACKJACK
def create_deck():
    '''
    create the deck of cards (ranks and suits) and shuffles it
    :return: the shuffled deck
    '''
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = []  # empty deck list

    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit)) #creates the deck and appends to the deck list

    random.shuffle(deck)  # shuffle the deck before returning
    return deck  # return the full deck after the loops finish and it was shuffled



def blackjack_game():
    '''
    simulates the blackjack game between the dealer and the player and determines the winner
    :return: nothing
    '''
    print("\n--- Blackjack ---")

    # initialize the deck and shuffles it
    deck = create_deck()
    random.shuffle(deck)

    #initial player and dealer hands
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    print(f"Dealer shows: {format_card(dealer_hand[0])}") #calls a function that tell the dealers first card
    print(f"Your hand: {format_hand(player_hand)} (Value: {calculate_hand_value(player_hand)})") #calls a function that tellse the player cards and value

    #player's turn
    while calculate_hand_value(player_hand) < 21: #if the value is below 21 the player can hit or stand
        move = input("Hit (H) or Stand (S)? ").strip().lower()
        if move == "h": #if he chooses to hit he gets one more card
            player_hand.append(deck.pop())
            print(f"Your hand: {format_hand(player_hand)} (Value: {calculate_hand_value(player_hand)})")
        elif move == "s":
            break
        else:
            print("Invalid input. Please enter 'H' or 'S'.")

    if calculate_hand_value(player_hand) > 21: #if the player has more than 21 he busts and he loses
        print("Bust! You lose!")
        return

    #dealer's turn
    print("\nDealer's turn.")
    while calculate_hand_value(dealer_hand) < 17: #when the value of the dealer's card is below 17 and the player has more the dealer hits
        dealer_hand.append(deck.pop())
        print(f"Dealer draws... {format_hand(dealer_hand)} (Value: {calculate_hand_value(dealer_hand)})")

    if calculate_hand_value(dealer_hand) > 21: #if the dealer has more than 21 he busts
        print("Dealer busts! You win!")
        return

    #determining the winner
    player_total = calculate_hand_value(player_hand)
    dealer_total = calculate_hand_value(dealer_hand)

    print(f"\nFinal Hands:\nYour hand ({player_total}): {format_hand(player_hand)}")
    print(f"Dealer's hand ({dealer_total}): {format_hand(dealer_hand)}")

    if player_total > dealer_total:
        print("You win!")
    elif player_total < dealer_total:
        print("Dealer wins. You lose!")
    else:
        print("It's a tie!")


#calculates the hand value
def calculate_hand_value(hand):
    '''
    receives the hand of cards of the dealer or player and calculate the value of it
    corrects the value of aces since aces can be valued 11 or 1 depending if the player or dealer has more than 21 or less
    :param hand: player's and dealer's hand of cards
    :return: the total value of the player's or dealer's hand of cards
    '''
    values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
              "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11} #dictionary of the ranks and its respectives values

    total = 0
    aces = 0

    # loop through the hands and sum the values in order to get total
    for card in hand:
        rank = card[0]  # extract the rank, since the suits doesn't matter
        total += values[rank] #sums the total according to the rank and values
        if rank == "A":
            aces += 1  # count aces since aces can be worth 11 or 1 for us to correct it after

    # convert aces from 11 to 1 if needed
    while total > 21 and aces > 0:
        #if the total is higher than 21 and there is at least 1 ace we change ace value from 11 to 1
        total -= 10 #converts aces value from 11 to 1
        aces -= 1 #take out the number of aces for the player not to be stuck in a loop

    return total

def format_card(card):
    '''
    formats the text that will appear to show the cards the player or dealer have
    :param card: the card of a hand
    :return: the rank and suit of the card
    '''
    return f"{card[0]} of {card[1]}"


def format_hand(hand):
    '''
    using the format_card it formats the hand of the dealer or player
    :param hand: the hand of the player or dealer
    :return: the hand of the player or dealer with the ranks and suits
    '''
    return ", ".join(format_card(card) for card in hand) #converts the list of cards into a single formatted string using the format_card() function

menu_casino() #calls the game
