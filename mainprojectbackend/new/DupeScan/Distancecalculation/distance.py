

from itertools import imap
import operator
import numarray
from math import*
from decimal import Decimal

#hamming distance calculation

def hamming3(str1, str2):
    assert len(str1) == len(str2)
    return sum(imap(operator.ne, str1, str2))

def numeric_hamming4(num1, num2):
    assert len(num1) == len(num2)
    return numarray.sum(num1 != num2)

# See http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/392115
def makeSigDigs(num, digits, debug=False):
    ...  ## not included here; only used to make pretty output
    return sig_string

def go(i):
    str1 = "A" * i
    str2 = str1[:i//2] + "B" + str1[i//2+1:]

    print i,

    t1 = time.time()
    assert hamming3(str1, str2) == 1
    hamming3(str1, str2)
    hamming3(str1, str2)
    hamming3(str1, str2)
    hamming3(str1, str2)
    hamming3(str1, str2)
    hamming3(str1, str2)
    hamming3(str1, str2)
    hamming3(str1, str2)
    hamming3(str1, str2)
    t2 = time.time()
    print makeSigDigs(t2-t1, 2),

    num1 = numarray.array(str1)
    num2 = numarray.array(str2)
    t1 = time.time()
    assert numeric_hamming4(num1, num2) == 1
    numeric_hamming4(num1, num2)
    numeric_hamming4(num1, num2)
    numeric_hamming4(num1, num2)
    numeric_hamming4(num1, num2)
    numeric_hamming4(num1, num2)
    numeric_hamming4(num1, num2)
    numeric_hamming4(num1, num2)
    numeric_hamming4(num1, num2)
    numeric_hamming4(num1, num2)
    t2 = time.time()
    print makeSigDigs(t2-t1, 2)

go(10)
go(100)
go(1000)
go(10000)
go(100000)
go(1000000)

 
class Similarity():
 
    """ Five similarity measures function """
 
    def euclidean_distance(self,x,y):
 
        """ return euclidean distance between two lists """
 
        return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))
 
    def manhattan_distance(self,x,y):
 
        """ return manhattan distance between two lists """
 
        return sum(abs(a-b) for a,b in zip(x,y))
 
    def minkowski_distance(self,x,y,p_value):
 
        """ return minkowski distance between two lists """
 
        return self.nth_root(sum(pow(abs(a-b),p_value) for a,b in zip(x, y)),
           p_value)
 
    def nth_root(self,value, n_root):
 
        """ returns the n_root of an value """
 
        root_value = 1/float(n_root)
        return round (Decimal(value) ** Decimal(root_value),3)
 
    def cosine_similarity(self,x,y):
 
        """ return cosine similarity between two lists """
 
        numerator = sum(a*b for a,b in zip(x,y))
        denominator = self.square_rooted(x)*self.square_rooted(y)
        return round(numerator/float(denominator),3)
 
    def square_rooted(self,x):
 
        """ return 3 rounded square rooted value """
 
        return round(sqrt(sum([a*a for a in x])),3)
 
    def jaccard_similarity(self,x,y):
 
    """ returns the jaccard similarity between two lists """
 
        intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
        union_cardinality = len(set.union(*[set(x), set(y)]))
        return intersection_cardinality/float(union_cardinality)

from similaritymeasures import Similarity
 
def main():
 
    """ the main function to create Similarity class instance and get used to it """
 
    measures = Similarity()
 
    print measures.euclidean_distance([0,3,4,5],[7,6,3,-1])
    print measures.jaccard_similarity([0,1,2,5,6],[0,2,3,5,7,9])
 
if __name__ == "__main__":
    main()

#pearson distance calculation

def pearson(pairs):
    # Takes in a list of pairwise ratings and produces a pearson similarity
    series_1 = [float(pair[0]) for pair in pairs]
    series_2 = [float(pair[1]) for pair in pairs]

    sum1 = sum(series_1)
    sum2 = sum(series_2)

    squares1 = sum([ n*n for n in series_1 ])
    squares2 = sum([ n*n for n in series_2 ])

    product_sum = sum([ n * m for n,m in pairs ])

    size = len(pairs)

    numerator = product_sum - ((sum1 * sum2)/size)
    denominator = sqrt((squares1 - (sum1*sum1) / size) * (squares2 - (sum2*sum2)/size))

    if denominator == 0:
        return 0
    
return numerator/denominator

