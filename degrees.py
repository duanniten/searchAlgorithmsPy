from degrees import Degress
import sys

degre = Degress()
def load_data(directory):
    degre.load_data(directory)

def person_id_for_name(name):
    return degre.person_id_for_name(name)

def shortest_path(source, target):
    degre.shortest_path()

def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    degre = Degress()

    # Load data from files into memory
    print("Loading data...")
    degre.load_data(directory)
    print("Data loaded.")

    degre.getSourceTarget()
    source = degre.source
    target = degre.target
    degre.shortest_path()
    degre.showResult()

if __name__ == "__main__":
    main()

