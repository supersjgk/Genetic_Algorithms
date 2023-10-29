import random

population_size = 50

genes = "10"

target = "101100111000"

class Individual():
	def __init__(self):
		self.chromosome = None
		self.fitness = None

	def bit_generate(self):
		global genes
		return random.choice(genes)

	def create_chromosome(self):
		global target
		self.chromosome = [self.bit_generate() for _ in range(len(target))]
		self.fitness = self.get_fitness()
		return self.chromosome

	def reproduce(self,parent2):
		child = []

		for mom_gene, dad_gene in zip(self.chromosome, parent2.chromosome):
			prob = random.random()
			
			if prob < 0.45:
				child.append(mom_gene)

			elif prob < 0.90:
				child.append(dad_gene)	
			
			else:
				child.append(self.bit_generate())

		ch = Individual()
		ch.chromosome = child
		ch.fitness = ch.get_fitness()
		return ch

	def get_fitness(self):
		global target
		fitness = 0
		for src, tar in zip(self.chromosome, target):
			if src != tar:
				fitness += 1
		return fitness

def main():
	global population_size
	generation = 1
	found = False
	population = []
	for _ in range(population_size):
		ind = Individual()
		chr = ind.create_chromosome()
		population.append(ind)
	#print(population[0], population[0].chromosome)

	while not found:
		population = sorted(population, key = lambda x:x.fitness)
		
		if population[0].fitness == 0:
			found = True
			break
		
		new_generation = []
		
		# top 10% of current generation go to next generation
		subset = int(population_size/10)
		for p in range(subset):
			new_generation.append(population[p])

		# top 50% reproduce to fill rest new generation
		rest = int(population_size*9/10)
		for _ in range(rest):	
			mom = random.choice(population[:50])
			dad = random.choice(population[:50])
			child =  mom.reproduce(dad)
			new_generation.append(child)
		
		population  = new_generation

		print(f'Generation: {generation}, String: {"".join(population[0].chromosome)}, Fitness: {population[0].fitness}')
		generation += 1

	print(f'Generation: {generation}, String: {"".join(population[0].chromosome)}, Fitness: {population[0].fitness}')

if __name__ == '__main__':
	main()

		

'''
Output looks like this
>python target_string.py
Generation: 1, String: 001101110000, Fitness: 3
Generation: 2, String: 001101110000, Fitness: 3
Generation: 3, String: 101100111110, Fitness: 2
Generation: 4, String: 101100111110, Fitness: 2
Generation: 5, String: 101100111110, Fitness: 2
Generation: 6, String: 101100110000, Fitness: 1
Generation: 7, String: 101100110000, Fitness: 1
Generation: 8, String: 101100110000, Fitness: 1
Generation: 9, String: 101100111000, Fitness: 0
'''
