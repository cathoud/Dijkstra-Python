class Nodo:
	def __init__(self,estado,custo,pai):
		self.estado = estado
		self.custo = custo
		self.pai = pai
	def __repr__(self):
		return '[Estado: %d - Custo: %.1f]' % (self.estado,self.custo)

	def getHash(self,table_size):
		return self.estado%table_size

	def __eq__(self,other):
		if(other != None):
			return self.estado == other.estado
		else:
			return False

	def __lt__(self,other):
		return self.custo < other.custo
