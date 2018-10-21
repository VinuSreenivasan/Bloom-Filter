import sys
import mmh3
import BitVector
import math

# Set default encoding to utf-8
reload(sys)
sys.setdefaultencoding('utf-8')

class countBloomFilter(object):
	def __init__(self, mn, k):
		if mn <= 0 or k <= 0:
			raise ValueError('Error: mn and k should be > 0')
		self.mn = mn 
		self.k = k
		self.n = 0 
		self.bitArray = []
		self._setAllBitsToZero()

	def _setAllBitsToZero(self):
		for i in range(0, self.mn):
			self.bitArray.append(0)

	def BAIndices(self, key):
		rl = []
		for i in range(1, self.k + 1):
			rl.append((hash(key) + i * mmh3.hash(key)) % self.mn)
		return rl
			
	#INCLUSION OF KEYS
	def addition(self, key):
		for i in self.BAIndices(key):
			self.bitArray[i] += 1
		self.n += 1

	#EXISTENCE OF THE KEY IN THE SET 
	def exist(self, key):
		for i in self.BAIndices(key):
			if self.bitArray[i] <= 0:
				return False
		return True		
	#LENGTH
	def length(self):
		return self.n

	#DELETION OF KEYS
	def delete(self, key):
		for i in self.BAIndices(key):
			self.bitArray[i] -= 1
		self.n -= 1

	def generatefinal_statistics(self):
		n = float(self.n)
		mn = float(self.mn)
		k = float(self.k)
		prob_false_pos = math.pow(1.0 - math.exp(-(k*n)/mn), k)
		print "Number of elements present in the filter: ", n
		print "Number of bits in filter: ", mn
		print "Number of hashes used in filter: ", k
		print "Probability of false positives present in the set: ", prob_false_pos
		print "Predicted false positive rate: ", prob_false_pos * 100.0
		

	def clear_filter(self):
		self.n = 0
		self.bv = BitVector.BitVector(size = self.mn)	
