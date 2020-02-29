from random import uniform, seed
from math import sqrt
import numpy
import math

class Strategy:
    def get_valuation(self, bid):
        return bid

class Percent_V_Strategy(Strategy):
    def __init__(self, percent):
        self.percent = percent

    def get_bid(self, valuation):
        return self.percent * valuation

        