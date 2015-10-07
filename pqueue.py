class Pqueue:
	def __init__(self):
		self.pqueue = []

	def push(self,val):
		self.pqueue.append(val)
		n = len(self.pqueue)
		while n!=1:
			if self.pqueue[n-1] < self.pqueue[int(n/2)-1] :
				val = self.pqueue[n-1]
				self.pqueue[n-1] = self.pqueue[int(n/2)-1]
				self.pqueue[int(n/2)-1] = val
			if n%2 == 1 and self.pqueue[n-2] < self.pqueue[int(n/2)-1] :
				val = self.pqueue[n-2]
				self.pqueue[n-2] = self.pqueue[int(n/2)-1]
				self.pqueue[int(n/2)-1] = val
			n = int(n/2)

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
