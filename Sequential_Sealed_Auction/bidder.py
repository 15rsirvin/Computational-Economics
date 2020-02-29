from random import uniform, seed
import math
import numpy
import random
import strategies

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