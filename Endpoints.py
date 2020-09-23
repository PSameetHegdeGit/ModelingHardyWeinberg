from Species import Species
from flask import *
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/<population>&<no_of_matings>")
def getGenerationalRatios(population, no_of_matings):
    species = Species(int(population))
    species.setAlleleCombos()
    for i in range(3):
        species.mate(int(no_of_matings))

    indices = [i for i in range(len(species.generations))]
    generations = dict(zip(indices, species.generations))

    print(generations)


    return generations








if __name__ == "__main__":

    app.run()