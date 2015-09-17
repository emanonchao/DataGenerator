import random
import math



'''def select_data(init_x, init_y, step, max_val, min_val, data):
	y = random.uniform(0, 100)
	x = init_x + step
	k = (y - init_y) / step
	if k > 0.5 or k < -0.5:
		select_data(init_x, init_y, step, max_val, min_val, data)
	else:
		if y < min_val or y > max_val:
			select_data(init_x, init_y, step, max_val, min_val, data)
		else:
			data.append([x, y])

def generate_data(amount, step, max_val, min_val, data):
	for i in range(0, amount-1):
		old_x = data[i][0]
		old_y = data[i][1]
		select_data(old_x, old_y, step, max_val, min_val, data)
	return data'''


class SpecificCurve(object):
	def __init__(self, init, min_val, max_val):
		self.x = 0
		self.y = init
		self.max = max_val
		self.min = min_val
		self.step = 5

	def walk(self, prev_x, prev_y, step):
		repeated_times = 0
		while True:
			y = random.uniform(0, 10000) / 10000 * (self.max - self.min) + self.min
			x = prev_x + step
			k = (y - prev_y) / step
			#print (x, y, k)
			if k > 0.5 or k < -0.5 or y < self.min or y > self.max:
				repeated_times += 1
				continue
			print repeated_times
			return (x, y)

	def generate_data(self, amount):
		data = []
		for i in range(0, amount-1):
			data.append(self.get_next_x_y())
		return data

	def get_next_x_y(self):
		(self.x, self.y) = self.walk(self.x, self.y, self.step)
		return (self.x, self.y)

	def get_next(self):
		(self.x, self.y) = self.walk(self.x, self.y, self.step)
		return self.y
