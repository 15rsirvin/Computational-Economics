from random import uniform, seed
import concurrent.futures
import math
import numpy
import random
import strategies
import time

seed(12)

class Bidder:
    def __init__(self, num_rounds, strat_list, dist_max):
        self.dist_max = dist_max
        self.draw_valuation()
        self.w = [1.0] * len(strat_list)
        self.eta = math.sqrt(math.log(len(strat_list))/num_rounds)
        self.strat_list = strat_list 

    total_utility = 0.0

    def draw_valuation(self):
        self.valuation = numpy.random.uniform(0, self.dist_max)
    
    def get_valuation(self):
        return self.valuation

    def update_weights(self, utilities):
        for i in range(len(self.w)):
            self.w[i] = (self.w[i] * (1 + (self.eta * utilities[i])))
    
    def draw(self):
        choice = random.uniform(0, sum(self.w))
        choice_index = 0

        for weight in self.w:
            choice -= weight
            if choice <= 0:
                return choice_index
            choice_index += 1
        print("error in draw")
        return -1


    def get_bid(self):
        choice_index = self.draw()
        bid =  strat_list[choice_index].get_bid(self.valuation)
        return bid

    def calculate_utilities(self, winning_price, is_winner):
        utilities = []
        for i in range(len(self.strat_list)):
            bid = strat_list[i].get_bid(self.valuation)
            #print("Strat: ", strat_list[i].percent, " Bid:", bid, " Winning Price", winning_price, " Valuation: ", self.valuation)
            if bid < winning_price:
                utilities.append(0)
            elif bid == winning_price and not is_winner:
                utilities.append(0)
            elif bid == winning_price and is_winner:
                utilities.append(self.valuation - bid)
            else:
                utilities.append(self.valuation - bid)
        #print(is_winner, utilities)
        return utilities
     
    def won(self, winning_price):
        self.total_utility += (self.valuation - winning_price)
        regret_utilities = self.calculate_utilities(winning_price, True)
        self.update_weights(regret_utilities)
        

    def lost(self, winning_price):
        regret_utilities = self.calculate_utilities(winning_price, False)
        self.update_weights(regret_utilities)
    
    def print_probs(self):
        sum_w = sum(self.w)
        for weight in self.w:
            print(weight / sum_w)

def max_list(array):
    max = 0
    for num in array:
        if num > max:
            max = num
    return max

#Takes list of bidders and the winning price
#Returns list of indecies of winning bidder(s) (helps with ties)
def get_winners_index(bids, winning_price):
    winners = []
    for i in range(len(bids)):
        if bids[i] == winning_price:
            winners.append(i)
    return winners

def sequential_auction(args):
    NUM_BIDDERS = args[0]
    NUM_ROUNDS = args[1]
    strat_list = args[2]
    # alice = Bidder(NUM_ROUNDS, strat_list, 1)
    # bob = Bidder(NUM_ROUNDS, strat_list, 1)
    bidders = []
    r = NUM_BIDDERS % 2
    for i in range((NUM_BIDDERS // 2) + r):
        bidders.append(Bidder(NUM_ROUNDS, strat_list, 1))
    for i in range(NUM_BIDDERS//2):
        bidders.append(Bidder(NUM_ROUNDS, strat_list, 2))

    total_social_welfare = 0
    optimal_social_welfare = 0
    POA_AVERAGE = 0

    for i in range(NUM_ROUNDS):
        bids = []
        valuations = []
        for bidder in bidders:
            bidder.draw_valuation()
            bids.append(bidder.get_bid())
            valuations.append(bidder.get_valuation())

        #Determine what bid won
        selling_price = max_list(bids)
        winning_bidders = get_winners_index(bids, selling_price)
        final_winner = random.choice(winning_bidders)

        #Determine what valuation should have won
        highest_valuation = max_list(valuations)

        #Update Agents on Outcome
        for j in range(len(bidders)):
            if j == final_winner:
                bidders[j].won(selling_price)
            else:
                bidders[j].lost(selling_price)

        #Update Social Welfare and POA values
        total_social_welfare += bidders[final_winner].get_valuation()
        optimal_social_welfare += highest_valuation
        POA = total_social_welfare/optimal_social_welfare
        if(POA_AVERAGE == 0):
            POA_AVERAGE = POA
        else:
            POA_AVERAGE = (POA + POA_AVERAGE)/2

        if(i == NUM_ROUNDS - 1):
            return POA
            
# == Stratagy Initialization == 
NUM_STRATS = 100
strat_list = []
for i in range(NUM_STRATS + 1):
    percent = i / NUM_STRATS
    strat_list.append(strategies.Percent_V_Strategy(percent))

# == Simulation Parameters ==
NUM_ROUNDS = 100000
MAX_NUM_BIDDERS = 100
NUM_SIMULATIONS = 100

# == Main ==
all_results = []
for i in range(2, MAX_NUM_BIDDERS+1):
    print("Number of Bidders: " , i)
    args = [(i, NUM_ROUNDS, strat_list)] * NUM_SIMULATIONS
    with concurrent.futures.ProcessPoolExecutor() as executer:
        results = executer.map(sequential_auction, args)
    temp_list = [result for result in results]
    all_results.append(temp_list)
numpy.savetxt('asymmetric_data.dat', all_results)