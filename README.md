# Computational Economics Thesis Code
The code in this respository was used for my senior thesis at Reed college on the price of anarchy in first price auctions. This contains three directories:

1.) **Sequential_Sealed_Auction**- contains the basic code and variations of the simulation of sequential (many in a row with the same agents and similar goods), first-price (highest bidder wins), sealed-bid (every one submits one secret bid) auctions.

2.) **Data** - contains the data saved from running each of the simulations. This is the data that is used to produce the graphs in my thesis.

3.) **Shellings_Segregation_Model** - contains the code for the recreation of Thomas Shelling segregation simulation used in thesis. This is a recreation of the code found [here](https://python.quantecon.org/) in Sargent and Stachurski's lectures on quantitative economics with Python.

## Sequential Auctions
The files in this folder are the bulk of my thesis. This is the simulation of sequential first price auctions were the agents are given an oppurtunity to learn after every round. The basic auction is called 'basic_auction.py', and all of the others are modifications of this to fit the needs of the thesis.

### zero intelligence auctions
The zero intelligence auctions (labeled zi) are ones where the bidder selects their bid randomly in a given. This range is either \[0,v\], the interval from 0 to their valuation,v, or \[0, 2v\] for overbidders.

### Learning Agent Auctions 
All auctions that are not zi auction, are auctions with learning agetns. The agents learn according to the multiplicative weights algorithm where they are picking between non-negative integer shades of their bids. That is choosing between bidding 0%, 1% ... 99%, 100% of their current valuation v_i.

## DATA
The data files in each auction is labeled according to the simulation that produced it. The code in the file is what was used to produce the graphs for the thesis. 

### Paramaters for each data file
None of the paramaters have been changed for these simulations since running them, but they are given below.

The first set of auctions (symmetric, zi_symmetric, assymetric, and zi_assymetric) were conducted with 100,000 rounds (T = 100000), up to 100 bidders, and 100 simulations at each of these values. This took approximatly 10 days to compute, so subsequent auctions were done with smaller values.

The second set of auctions (overbidding and zi_overbidding) were conducted with 10,000 rounds (T=10000), up to 100 bidders, and 10 runs at each value (m =10). 