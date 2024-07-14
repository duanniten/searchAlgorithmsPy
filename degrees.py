from degrees import Degress
import sys


def load_data(directory):
    degre = Degress()
    degre.load_data(directory)

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
    degre.shortest_path()
    degre.showResult()

if __name__ == "__main__":
    main()

