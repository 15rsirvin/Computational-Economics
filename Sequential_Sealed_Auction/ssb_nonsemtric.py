from random import uniform, seed
from math import sqrt
import numpy
import math
import random

seed(12)

class Bidder:
    def __init__(self, dist):
        self.dist = dist #not used yet, need to make modular
        self.draw_valuation()
    
    total_utility = 0

    def draw_valuation(self):
        if self.dist == 0:
            self.valuation = numpy.random.uniform(0,1)
        else:
            self.valuation = numpy.random.uniform(0,1)
    
    def get_valuation(self):
        return self.valuation

    # def get_bid(self):
    #     self.bid = (0.5) * self.valuation
    #     return self.bid

    def get_bid(self):
        if self.dist == 0:
            self.bid = ((4/ (3*self.valuation)) * (1 - math.sqrt(1 - ((3 * self.valuation**2) / 4))))
        else:
            self.bid = ((4/ (3*self.valuation)) * (math.sqrt(1+ ((3 * self.valuation**2) / 4)) - 1))
        return self.bid

    def won(self, winning_price):
        utility = (winning_price - self.valuation)
        self.total_utility += utility

    def lost(self):
        return

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

# == Main == #

alice = Bidder(0)
bob = Bidder(1)
bidders = [alice, bob]
total_social_welfare = 0
optimal_social_welfare = 0
POA_AVERAGE = 0

for i in range(100000):
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
            bidders[j].lost()

    #Update Social Welfare and POA values
    total_social_welfare += bidders[final_winner].get_valuation()
    optimal_social_welfare += highest_valuation
    POA = total_social_welfare/optimal_social_welfare

    POA_AVERAGE = (POA_AVERAGE + POA)/2

    if(i == 0 or i == 9 or i == 999 or i == 9999 or i == 99999):
        print('Loop', i+1,  final_winner, "POA: ", POA, "POA AVG: ", POA_AVERAGE) 




    







































































