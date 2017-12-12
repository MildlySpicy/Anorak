"""Random testing file"""


class uhh:
	inting: int
	stringing: str
	floating: float

	def __init__(self) -> None:
		self.inting = 123
		self.stringing = "memes123"
		self.floating = 1.23

	def __str__(self) -> str:
		return self.stringing + str(self.inting)


if __name__ == '__main__':
	bob = uhh()
	print(str(bob))