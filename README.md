# Computational Economics Thesis Code
The code in this respository was used for my senior thesis at Reed college on the price of anarchy in first price auctions. This contains three directories:

1.) **Sequential_Sealed_Auction**- contains the basic code and variations of the simulation of sequential (many in a row with the same agents and similar goods), first-price (highest bidder wins), sealed-bid (every one submits one secret bid) auctions.

2.) **Data** - contains the data saved from running each of the simulations. This is the data that is used to produce the graphs in my thesis.

3.) **Shellings_Segregation_Model** - contains the code for the recreation of Thomas Shelling segregation simulation used in thesis. This is a recreation of the code found here [title](https://python.quantecon.org/) in Sargent and Stachurski's lectures on quantitative economics with Python.

## Sequential Auctions
The files in this folder are the bulk of my thesis. This is the simulation of sequential first price auctions were the agents are given an oppurtunity to learn after every round. The basic auction is called 'basic_auction.py', and all of the others are modifications of this to fit the needs of the thesis.

### zero intelligence auctions
The zero intelligence auctions are ones where the bidder selects their bid randomly in a given range. There