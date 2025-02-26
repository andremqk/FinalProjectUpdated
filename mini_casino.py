import random

# ROULETTE
# defining the red numbers of the roulette (0 is green)
red_numbers = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}


def menu_casino(balance):
    '''
    this function displays the menu of the casino showing the user possible selections.
    the user can select to play blackjack or roulette, check balance, deposit and withdraw money, and exit.

    :param balance: the amount of money available of the player
    :return: the updated balance after the player interacted with the casino
    '''
    while True:  # means that the code/game will repeat until the user breaks
        print("\nWelcome to the Mini Casino! Deposit money to begin playing.")
        print("1. Play Roulette")
        print("2. Play Blackjack")
        print("3. My Balance")
        print("4. Deposit Money")
        print("5. Withdraw Money")
        print("0. Exit the casino")
        choice = input("Enter your choice: ").strip()  # the strip() is used to correct possible spaces

        if choice == "1":
            balance = roulette_game(balance)
        elif choice == "2":
            balance = blackjack_game(balance)
        elif choice == "3":
            print(f"\nYour current balance is: {balance}")
        elif choice == "4":
            balance = deposit(balance)
        elif choice == "5":
            balance = withdraw(balance)
        elif choice == "0":
            print("Thanks for coming! Goodbye.")
            break  # takes the player out of the game if he presses 0
        else:
            print("Invalid option. Please choose an valid option.")
    return balance


def deposit(balance):
    '''
    the user can deposit an amount, the function also validates the input,
    and updates the player's balance if the amount is positive.
    :param balance: the current balance before the deposit
    :return: the updated balance after the player's deposit
    '''
    try:
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            print(f"Successfully deposited ${amount}. New balance: ${balance}")
        else:
            print("Deposit amount must be positive.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    return balance


def withdraw(balance):
    '''
    the user can withdraw an amount, the function also validates the input,
    and updates the player's balance if the amount is positive and lower or equal
    to the player's current balance.
    :param balance: the current balance before the withdraw
    :return: the updated balance after the player's withdraw
    '''
    try:
        amount = float(input("Enter withdrawal amount: "))
        if amount > 0 and amount <= balance:
            balance -= amount
            print(f"Successfully withdrew ${amount}. New balance: ${balance}")
        elif amount > balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    return balance


def roulette_game(balance):
    '''
    roulette game where the user places a bet on either a specific number (0-36) or a color (red or black).
    the function validates the bet amount against the current balance, spins the roulette wheel to generate a result.
    After it updates the balance based on the result.

    :param balance: player's current balance before placing the bet.
    :return: updated balance after the game. winning bets add the value of the win to the balance,
               while losing bets subtract the bet amount.
    '''
    print("\n--- Roulette ---")
    print(f"Your balance: ${balance}")
    try:
        bet_amount = float(input("Enter your bet amount: "))
        if bet_amount > balance or bet_amount <= 0:
            print("Invalid bet amount.")
            return balance
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return balance
    print("Bet Options:")
    print("1. Bet on a specific number (0-36)")
    print("2. Bet on a color (red or black)")

    bet_type = input("Choose your bet type (1 or 2): ").strip()

    if bet_type == "1":
        # bet on a number
        try:
            user_number = int(input("Enter the number you want to bet on (0-36): ").strip())
            if user_number < 0 or user_number > 36:
                print("Number must be between 0 and 36!")
                return balance
        except ValueError:
            print("Invalid input. Please enter an integer between 0 and 36.")
            return balance
    elif bet_type == "2":
        # bet on a color
        user_color = input("Enter the color you want to bet on (red or black): ").strip().lower()
        if user_color not in {"red", "black"}:
            print("Invalid color. Please choose either 'red' or 'black'.")
            return balance
    else:
        print("Invalid bet type selected.")
        return balance

    # spins the roulette and gives a number and its respective color
    result_number = random.randint(0, 36)
    if result_number == 0:
        result_color = "green"
    elif result_number in red_numbers:  # if the number is in the list we defined in the beginning as red_numbers is red
        result_color = "red"
    else:
        result_color = "black"

    print(f"\nThe roulette wheel spins and lands on {result_number} ({result_color})!")

    # results
    if bet_type == "1":  # if he chooses to bet in a number
        if result_number == user_number:
            print(f"Congratulations! Your number hit. You won {winnings}!")
            return balance + bet_amount * 35
        else:
            print(f"Sorry, your number did not hit. Better luck next time! You lost {bet_amount}")
            return balance - bet_amount
    else:  # if he chooses to bet in a color
        if result_color == user_color:
            print(f"Congratulations! The color matches. You won {bet_amount * 2}!")
            return balance + bet_amount
        else:
            print(f"Sorry, the color doesn't match. You lost {bet_amount}.")
            return balance - bet_amount


# BLACKJACK
def create_deck():
    '''
    creates a deck of cards (52 cards, ranks and suits) and shuffles it
    :return: the shuffled deck list of tuples, where each contains a rank and a suit.
    '''
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = []  # empty deck list

    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))  # creates the deck and appends to the deck list

    random.shuffle(deck)  # shuffle the deck before returning
    return deck  # return the full deck after the loops finish and it was shuffled


def blackjack_game(balance):
    '''
    simulates the blackjack game between the dealer and the player, allows the player to place a bet,
    make hit and stand decisions, then resolving the dealer's hand according to blackjack rules
    and determines the winner. The function at the end updates the balance according to the result

    :param balance: player's current balance before starting the game.
    :return: updated balance after the game, reflecting any winnings or losses from the bet.
    '''
    print("\n--- Blackjack ---")
    print(f"Your balance: ${balance}")

    # how much the user is going to bet
    try:
        bet_amount = float(input("Enter your bet amount: "))
        if bet_amount > balance or bet_amount <= 0:
            print("Invalid bet amount.")
            return balance
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return balance

    # initialize the deck and shuffles it
    deck = create_deck()
    random.shuffle(deck)

    # initial player and dealer hands
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    print(f"Dealer shows: {format_card(dealer_hand[0])}")  # calls a function that tell the dealers first card
    print(
        f"Your hand: {format_hand(player_hand)} (Value: {calculate_hand_value(player_hand)})")  # calls a function that tellse the player cards and value

    # player's turn
    while calculate_hand_value(player_hand) < 21:  # if the value is below 21 the player can hit or stand
        move = input("Hit (H) or Stand (S)? ").strip().lower()
        if move == "h":  # if he chooses to hit he gets one more card
            player_hand.append(deck.pop())
            print(f"Your hand: {format_hand(player_hand)} (Value: {calculate_hand_value(player_hand)})")
        elif move == "s":
            break
        else:
            print("Invalid input. Please enter 'H' for hit or 'S' for stand.")

    if calculate_hand_value(player_hand) > 21:  # if the player has more than 21 he busts and he loses
        print(f"Bust! You lost {bet_amount}.")
        return balance - bet_amount

    # dealer's turn
    print("\nDealer's turn.")
    while calculate_hand_value(
            dealer_hand) < 17:  # when the value of the dealer's card is below 17 and the player has more the dealer hits
        dealer_hand.append(deck.pop())
        print(f"Dealer draws... {format_hand(dealer_hand)} (Value: {calculate_hand_value(dealer_hand)})")

    if calculate_hand_value(dealer_hand) > 21:  # if the dealer has more than 21 he busts
        print(f"Dealer busts! You won {bet_amount * 2}!")
        return balance + bet_amount

    # determining the winner
    player_total = calculate_hand_value(player_hand)
    dealer_total = calculate_hand_value(dealer_hand)

    print(f"\nFinal Hands:\nYour hand ({player_total}): {format_hand(player_hand)}")
    print(f"Dealer's hand ({dealer_total}): {format_hand(dealer_hand)}")

    if player_total > dealer_total:
        print(f"You won {bet_amount * 2}!")
        return balance + bet_amount
    elif player_total < dealer_total:
        print(f"Dealer wins. You lost {bet_amount}!")
        return balance - bet_amount
    else:
        print("It's a tie!")
        return balance


# calculates the hand value
def calculate_hand_value(hand):
    '''
    receives the hand of cards of the dealer or player and calculate the value of it,
    adjusting the value of aces as needed.
    :param hand: list of tuples representing the cards in a hand.
                 each tuple consists of a rank and a suit
    :return: total value of the hand. Aces are initially counted as 11, but if the total exceeds 21,
             each ace's value is reduced from 11 to 1 until the total is 21 or lower.
    '''
    values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
              "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10,
              "A": 11}  # dictionary of the ranks and its respectives values

    total = 0
    aces = 0

    # loop through the hands and sum the values in order to get total
    for card in hand:
        rank = card[0]  # extract the rank, since the suits doesn't matter
        total += values[rank]  # sums the total according to the rank and values
        if rank == "A":
            aces += 1  # count aces since aces can be worth 11 or 1 for us to correct it after

    # convert aces from 11 to 1 if needed
    while total > 21 and aces > 0:
        # if the total is higher than 21 and there is at least 1 ace we change ace value from 11 to 1
        total -= 10  # converts aces value from 11 to 1
        aces -= 1  # take out the number of aces for the player not to be stuck in a loop

    return total


def format_card(card):
    '''
    formats a card tuple into a string for the player to read displaying its rank and suit.

    :param card: the card of a hand, a tuple where the first element is the rank and the second is a suit
    :return: a string representation of the rank and suit of the card
    '''
    return f"{card[0]} of {card[1]}"


def format_hand(hand):
    '''
    formats a list of cards into a single string by converting each card into a string
    using the format_card function, then joining them with commas.

    :param hand: list of card tuples, where each tuple contains a rank and a suit.
    :return: string representing the hand, with each card
             displayed as "rank" of "suit" as defined im function format_card and separated by commas.
    '''
    return ", ".join(format_card(card) for card in
                     hand)  # converts the list of cards into a single formatted string using the format_card() function


menu_casino(0)  # calls the game with an initial balance of 0