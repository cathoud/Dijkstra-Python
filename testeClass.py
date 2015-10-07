class Nodo:
	def __init__(self,estado,custo,pai):
		self.estado = estado
		self.custo = custo
		self.pai = pai
	def __repr__(self):
		return '[Estado: %d - Custo: %d]' % (self.estado,self.custo)

	def getHash(self,table_size):
		return self.estado%table_size

	def __eq__(self,other):
		return self.estado == other.estado

	def __lt__(self,other):
		return self.custo < other.custo

l = [[0,1,1,0,0,0,0,0],
	 [0,0,1,0,0,0,1,0],
	 [0,0,0,0,0,1,0,0],
	 [0,0,0,0,1,1,0,0],
	 [1,0,0,0,1,1,0,0],
	 [1,1,0,0,1,1,0,0],
	 [1,1,0,0,1,0,0,0],
	 [0,0,0,0,0,0,0,1]]

class Pqueue:
	def __init__(self):
		self.pqueue = []

	def push(self,val):
		self.pqueue.append(val)
		n = len(self.pqueue)
		while n!=1:
			if self.pqueue[n-1] < self.pqueue[n/2-1] :
				val = self.pqueue[n-1]
				self.pqueue[n-1] = self.pqueue[n/2-1]
				self.pqueue[n/2-1] = val
			if n%2 == 1 and self.pqueue[n-2] < self.pqueue[n/2-1] :
				val = self.pqueue[n-2]
				self.pqueue[n-2] = self.pqueue[n/2-1]
				self.pqueue[n/2-1] = val
			n = n/2

	def pop(self):
		n = len(self.pqueue)
		if n <= 0:
			return None
		top = self.pqueue[0]
		self.pqueue[0] = self.pqueue[n-1]
		del self.pqueue[n-1]
		n -= 1
		
		i = 1
		while i <= n/2:
			val = self.pqueue[i-1]
			if 2*i < n:
				if self.pqueue[2*i-1] < self.pqueue[2*i]:
					if self.pqueue[2*i-1] < self.pqueue[i-1]:
						self.pqueue[i-1] = self.pqueue[2*i-1]
						self.pqueue[2*i-1] = val
						i = 2*i
					else:
						return top
				else:
					if self.pqueue[2*i] < self.pqueue[i-1]:
						self.pqueue[i-1] = self.pqueue[2*i]
						self.pqueue[2*i] = val
						i = 2*i+1
					else:
						return top
			else:
				if self.pqueue[2*i-1] < self.pqueue[i-1]:
					self.pqueue[i-1] = self.pqueue[2*i-1]
					self.pqueue[2*i-1] = val
					i = 2*i
				else:
					return top
		return top

	def empty(self):
		return len(self.pqueue) == 0

class Hash:
	def __init__(self,size):
		self.table = []
		for n in range(size):
			self.table.append([])

	def insert(self, newRecord):
		index = newRecord.getHash(len(self.table))
		self.table[index].append(newRecord)


	def find(self,record):
		index = record.getHash(len(self.table))
		for n in range(len(self.table[index])):
			if(record==self.table[index][n]):
				return self.table[index][n]
		return None

	def erase(self,record):
		index = record.getHash(len(self.table))
		for n in range(len(self.table[index])):
			if(record == self.table[index][n]):
				del self.table[index][n]

