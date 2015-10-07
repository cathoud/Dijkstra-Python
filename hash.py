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
