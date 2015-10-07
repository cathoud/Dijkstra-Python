class Mapa:
	def __init__(self,rows,columns):
		self.mapa = []
		for n in range(rows):
			self.mapa.append([None]*columns)

	def estado(self,t):
		return t[1] * len(self.mapa) + t[0]

	def r_estado(self,est):
		return (int(est%len(self.mapa)),int(est/len(self.mapa)))