import csv
import sys

from frontier import QueueFrontier
from node import Node

class Degress():
    def __init__(self) -> None:
            # Maps names to a set of corresponding person_ids
        self.names = {}

    # Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
        self.people = {}

    # Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
        self.movies = {}
        self.path= None
        self.frontier = QueueFrontier()
        self.num_explored =0
        self.explored = set()
        pass



    def load_data(self,directory):
        """
        Load data from CSV files into memory.
        """
        # Load people
        with open(f"{directory}/people.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.people[row["id"]] = {
                    "name": row["name"],
                    "birth": row["birth"],
                    "movies": set()
                }
                if row["name"].lower() not in self.names:
                    self.names[row["name"].lower()] = {row["id"]}
                else:
                    self.names[row["name"].lower()].add(row["id"])

        # Load movies
        with open(f"{directory}/movies.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.movies[row["id"]] = {
                    "title": row["title"],
                    "year": row["year"],
                    "stars": set()
                }

        # Load stars
        with open(f"{directory}/stars.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    self.people[row["person_id"]]["movies"].add(row["movie_id"])
                    self.movies[row["movie_id"]]["stars"].add(row["person_id"])
                except KeyError:
                    pass


    def getSourceTarget(self):

        self.source = self.person_id_for_name(input("Name: "))
        if self.source is None:
            sys.exit("Person not found.")
        self.target = self.person_id_for_name(input("Name: "))
        if self.target is None:
            sys.exit("Person not found.")

    
    
    def showResult(self):
        if self.path is None:
            print("Not connected.")
        else:
            degrees = len(self.path)
            print(f"{degrees} degrees of separation.")
            path = [(None, self.source)] + self.path
            for i in range(degrees):
                person1 = self.people[path[i][1]]["name"]
                person2 = self.people[path[i + 1][1]]["name"]
                movie = self.movies[path[i + 1][0]]["title"]
                print(f"{i + 1}: {person1} and {person2} starred in {movie}")


    def shortest_path(self):
        """
        Returns the shortest list of (movie_id, person_id) pairs
        that connect the source to the target.

        If no possible path, returns None.
        """
        
        self.frontier.add(
            Node(
                state = self.source,
                parent = None,
                action = None,
                neighboards= self.neighbors_for_person(self.source)
            )
        )
        while True:
            if self.frontier.empty():
                raise Exception('no solution')
            
            node = self.frontier.remove()
            self.num_explored += 1

            if node.state == self.target:
                
                self.path = []
                
                while node.parent is not None:
                    self.path.append((node.action, node.state))
                    node = node.parent
                self.path.reverse()
                return
                         
            self.explored.add(node.state)

            
            if len(node.neighboards) == 0:
                raise Exception ('no neigboards')
            
            for movie, neighboard in node.neighboards:
                if (
                    not self.frontier.containState(neighboard) and
                    neighboard not in self.explored
                    ):
                 
                    neighboards = self.neighbors_for_person(neighboard)
                    
                    self.frontier.add(Node(
                        state = neighboard,
                        parent = node,
                        action = movie,
                        neighboards = neighboards
                    ))



    def person_id_for_name(self, name):
        """
        Returns the IMDB id for a person's name,
        resolving ambiguities as needed.
        """
        person_ids = list(self.names.get(name.lower(), set()))
        if len(person_ids) == 0:
            return None
        elif len(person_ids) > 1:
            print(f"Which '{name}'?")
            for person_id in person_ids:
                person = self.people[person_id]
                name = person["name"]
                birth = person["birth"]
                print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
            try:
                person_id = input("Intended Person ID: ")
                if person_id in person_ids:
                    return person_id
            except ValueError:
                pass
            return None
        else:
            return person_ids[0]


    def neighbors_for_person(self, person_id):
        """
        Returns (movie_id, person_id) pairs for people
        who starred with a given person.
        """
        
        movie_ids = self.people[person_id]["movies"]
        neighbors = set()
        for movie_id in movie_ids:
            for person_id in self.movies[movie_id]["stars"]:

                if person_id == self.target:
                    self.frontier = QueueFrontier()
                    neighbors = set()
                    neighbors.add((movie_id, person_id))

                    return neighbors

                neighbors.add((movie_id, person_id))

        return neighbors