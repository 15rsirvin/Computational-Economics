from random import randint
pll = 1
pul = 10 

class Agent:
    def __init__(self):
        self.reservation = 4


class Buyer(Agent):
    def __init__(self):
        self.demand = 10
        self.curr_goods = 0

    def get_demand(self):
        return self.demand

    def submit_bid(self):
        return randint(pll, pul)

class Seller(Agent):
    def __init__(self):
        self.inventory = 10

    def get_supply(self):
        return self.inventory
    
    def submit_ask(self):
        return randint(pll, pul)

def get_total_demand(buyers):
    tot = 0
    for buyer in buyers:
        tot += buyer.get_demand()
    return tot

def get_total_supply(sellers):
    tot = 0
    for seller in sellers:
        tot += seller.get_supply()
    return tot

def main():
    buyers = [Buyer() for i in range(3)]
    sellers = [Seller() for i in range(3)]
    demand = get_total_demand(buyers)
    supply = get_total_supply(sellers)
    r = 0
    while r < min(supply, demand):
        oa = pul
        ob = pll
        while True:
            o_bidder = -1
            o_asker = -1
            bids = [buyers[i].submit_bid() for i in range(len(buyers))]
            asks = [sellers[i].submit_ask() for i in range(len(sellers))]
            
            for i in range(len(bids)):
                if bids[i] > ob and bids[i] < pul:
                    ob = bids[i]
                    o_bidder = i

            for i in range(len(asks)):
                if asks[i] > oa and asks[i] > pll:
                    oa = asks[i]

            if ob > oa:
                print("Round " + r)
                print("Bid is:" + ob)
                print("Ask is:" + oa)
                break
        r += 1
    
main()
            


        


