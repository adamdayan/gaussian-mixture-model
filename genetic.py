import copy
import random

class Mastermind:
    def __init__(self, target_list):
        self.target_list = target_list

    def score(self, suggestion_list):
        running_score = 0.00

        this_target_list = copy.deepcopy(self.target_list)

        cnt = 0
        
        for suggested_gene, target_gene in zip(suggestion_list, this_target_list):
            if suggested_gene == target_gene:
                this_target_list[cnt] = '999'
                running_score += 1

            cnt+= 1
                
        if running_score != len(self.target_list):
            for suggested_num, suggested_gene in enumerate(suggestion_list):
                for target_num, target_gene in enumerate(this_target_list):
                    if suggested_gene == target_gene and target_num != suggested_num:
                        running_score += 0.5


        return running_score

class GeneticSoup:
    def __init__(self, pop_size, mastermind):
        self.pop_size = pop_size
        self.phenolist = []
        self.mastermind = mastermind

        for x in range(self.pop_size):
            phenotype = {}
            phenotype["geno"] = []
            for x in range(4):
                holding_string = [str(random.randint(0,1)) for i in range(3)]
                holding_string = ''.join(holding_string)
                phenotype["geno"].append(holding_string)

            self.phenolist.append(phenotype)


    def evaluate(self):
        for phenotype in self.phenolist:
            phenotype["fitness"] = self.mastermind.score(phenotype["geno"])

    def roulette(self):
        total_fitness = 0
        for phenotype in self.phenolist:
            total_fitness += phenotype["fitness"]

        fitprob_running_total = 0
        cumprob_list = []

        for phenotype in self.phenolist:
            phenotype["fitprob"] = phenotype["fitness"] / total_fitness
            fitprob_running_total += phenotype["fitprob"]
            phenotype["cumprob"] = fitprob_running_total
            cumprob_list.append(fitprob_running_total)

        self.parents = []

        for x in range(len(self.phenolist)):
            r = random.uniform(0, max(cumprob_list))
            for cnt, cp in enumerate(cumprob_list):
                if cp >= r:
                    self.parents.append(self.phenolist[cnt])
                    break

        
    def breed(self):
        self.phenolist.clear()

        for idx in range(0, len(self.parents) - 1, 2):
            parent1 = self.parents[idx]["geno"]
            parent2 = self.parents[idx + 1]["geno"]

            parent1_string = ''.join(parent1)
            parent2_string = ''.join(parent2)

            crossover_idx = random.randint(0, len(parent1_string))

            child1_string = list(parent1_string[:crossover_idx] + parent2_string[crossover_idx:])
            child2_string = list(parent2_string[:crossover_idx] + parent1_string[crossover_idx:])

            m = 1/len(child1_string)
            
            for idx in range(len(child1_string)):
                mutation_decider = random.uniform(0, 1)
                if mutation_decider < m:
                    if child1_string[idx] == '0':
                        child1_string[idx] = '1'
                    else:
                        child1_string[idx] = '0'

                mutation_decider = random.uniform(0, 1)
                if mutation_decider < m:
                    if child2_string[idx] == '0':
                        child2_string[idx] = '1'
                    else:
                        child2_string[idx] = '0'


            ''.join(child1_string)
            ''.join(child2_string)
                        
            n = 3
            child1 = {"geno":[''.join(child1_string[i:i+n])
                              for i in range(0, len(child1_string), n)]}
            child2 = {"geno":[''.join(child2_string[i:i+n])
                              for i in range(0, len(child2_string), n)]}
            self.phenolist.append(child1)
            self.phenolist.append(child2)


    def evolve_loop(self):
        max_fitness = 0.0
        best_pheno = {}

        self.evaluate()
        while max_fitness != 4.0:
            self.roulette()
            self.breed()
            self.evaluate()

            for pheno in self.phenolist:
                if pheno["fitness"] > max_fitness:
                    max_fitness = pheno["fitness"]
                    best_pheno = pheno

        print(best_pheno)
            


            

if __name__ == "__main__":
    target_list = ['000', '011','111','001']
    suggestion_list = ['011', '011','111','001']
    
    m = Mastermind(target_list)
    
    score = m.score(suggestion_list)

    soup = GeneticSoup(10, m)

    soup.evolve_loop()

    
    
