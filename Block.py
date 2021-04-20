class Block:
	def __init__(self, mass, velocity, position, shape, col):
		self.mass = mass
		self.velocity = velocity
		self.position = position
		self.shape = shape
		self.col = col

	def draw(self, objct):
		objct.shape("square")
		objct.color(self.col)
		objct.shapesize(self.shape, self.shape)
		objct.penup()
		objct.setposition(self.position[0], self.position[1])

	def update(self):
		self.position += self.velocity
