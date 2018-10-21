import sys
import mmh3
import BitVector
import math

# Set default encoding to utf-8
reload(sys)
sys.setdefaultencoding('utf-8')

class BloomFilter(object):
	def __init__(self, mn, k):
		if mn <= 0 or k <= 0:
			raise ValueError('Error: mn and k should be > 0')
		self.mn = mn
		self.k = k
		self.n = 0
		self.bv = BitVector.BitVector(size = self.mn)
		self._setAllBitsToZero()

	def _setAllBitsToZero(self):
		for i in self.bv:
			self.bv[i] = 0

	def BAIndices(self, key):
		rl = []
		for i in range(1, self.k + 1):
			rl.append((hash(key) + i * mmh3.hash(key)) % self.mn)
		return rl

	def addition(self, key):
		for i in self.BAIndices(key):
			self.bv[i] = 1
		self.n += 1

	def exist(self, key):
		for i in self.BAIndices(key):
			if self.bv[i] != 1:
				return False
		return True

	def length(self):
		return self.n

	def generatefinal_statistics(self):
		n = float(self.n)
		mn = float(self.mn)
		k = float(self.k)
		prob_false_pos = math.pow((1.0 - math.exp(-(k*n)/mn)), k)
		print "Number of elements entered in filter: ", n
		print "Number of bits in filter: ", mn
		print "Number of hashes in filter: ", k
		print "Probability of false positives: ", prob_false_pos
		print "Predicted false positive rate: ", prob_false_pos * 100.0

	def clear_filter(self):
		self.n = 0
		self.bv = BitVector.BitVector(size = self.mn)
