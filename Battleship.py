def place_ship():
    print("placing ship ...")



if __name__ == '__main__':
    print("Battleship")

    array_1 = [["S", " ", " ", " ", " "],
               ["S", " ", " ", " ", " "],
               [" ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " "]]

    array_2 = [[" ", " ", " ", " ", " "],
               [" ", " ", " ", "S", "S"],
               [" ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " "]]

    place_ship(array_1, 15, "R")
