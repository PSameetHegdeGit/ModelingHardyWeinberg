import random



class Species:

    genoTypeList = []
    alleleList = []
    generations = []
    currentGenoTypeRatios = {}
    nextGenoTypeRatios = {}

    def __init__(self, population, no_of_alleles=2, letter="A"):
        self.no_of_alleles = no_of_alleles
        self.population = population
        self.letter = letter


    #Generates possible genotypes and creates number of members in population
    def setAlleleCombos(self):
        if (self.no_of_alleles == 2):
            self.alleleList.append(self.letter.upper())
            self.alleleList.append(self.letter.lower())

        #TODO: Do the multi Allele Case later
        else:
            print("multi-allele case")

        print("Alleles: " + str(self.alleleList))

        for allele in range(len(self.alleleList)):
            for allele1 in range(allele, len(self.alleleList)):
                self.genoTypeList.append((self.alleleList[allele] + self.alleleList[allele1]))

        print("Genotypes: " + str(self.genoTypeList))

        genoTypeDictionary = {}

        remove = 0
        length = len(self.genoTypeList)
        leftOver = self.population
        for index in range(length - 1):
            leftOver = leftOver - remove
            randomNumber = random.randint(0, leftOver)
            genoTypeDictionary[self.genoTypeList[index]] = randomNumber/self.population
            remove = randomNumber

        genoTypeDictionary[self.genoTypeList[length - 1]] = (self.population - remove)/self.population
        self.generations.append(genoTypeDictionary)
        self.currentGenoTypeRatios = genoTypeDictionary


    #Mates members of a species x amount of times --> Generate x amount of members in a population
    def mate (self, no_of_matings):

        alleles = list(self.currentGenoTypeRatios.keys())
        frequencies = list(self.currentGenoTypeRatios.values())

        self.nextGenoTypeRatios = dict.fromkeys(self.currentGenoTypeRatios,0) #Dict.fromkeys() produces a new dictionary that sets all items of old dictionary to 0


        for matingCount in range(no_of_matings + 1):
            genotype_Selection1 = random.choices(alleles, frequencies)[0]

            genotype_Selection2 = random.choices(alleles, frequencies)[0]

            newGenotype = random.choices(genotype_Selection1)[0] + random.choices(genotype_Selection2)[0]

            if (newGenotype == "aA"):
                newGenotype = "Aa"


            self.nextGenoTypeRatios[newGenotype] += 1

        print(self.nextGenoTypeRatios)
        self.currentGenoTypeRatios = self.nextGenoTypeRatios

        for v in self.currentGenoTypeRatios.keys():
            self.currentGenoTypeRatios[v] = self.currentGenoTypeRatios[v]/no_of_matings

        self.generations.append(self.currentGenoTypeRatios)
        print(self.generations)



if __name__ == "__main__":
    species = Species(int(50))
    species.setAlleleCombos()
    for i in range(3):
        species.mate(int(50))

    print(species.generations)
    indices = [i for i in range(len(species.generations))]
    generations = dict(zip(indices, species.generations))

    print(generations)






'''
 
        #Show that random is working properly
        alleleFrequencies = [0, 0, 0]
        for i in range (10000):
            result = random.choices(alleles, frequencies)
            if result[0] == "AA":
                alleleFrequencies[0]+=1
            elif result[0] == "Aa":
                alleleFrequencies[1]+=1
            else:
                alleleFrequencies[2]+=1

'''