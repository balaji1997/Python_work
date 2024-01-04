"""
    IPL statistics menu is shown for the user to select the Numerical or Statistical Analysis and to call the respective functions.

    Student ID: A00315875
    Date: 20/12/2023
"""
from NumericalAnalysis import *
from CategoricalAnalysis import *
if __name__ == "__main__":
    runs_list = []
    highscores_list = []
    team_sixes_dict = {}
    team_frequency_dict = {}
    try:
        with open("IPL_Stats-2023.csv") as file:
            headings=file.readline()
            try:
                for line in file:
                    #print(line.strip().split(","))
                    positions, players, teams, matches, notouts, runs, highscores, centuries, numberof4s, numberof6s=line.strip().split(",")
                    #print(int(runs))
                    try:
                        runs_list.append(int(runs))
                    except ValueError:
                        print("Unable to convert runs...", line)
                    try:
                        highscores_list.append(int(highscores))
                    except ValueError:
                        print("Unable to convert highscores...", highscores)
                    try:
                        if not teams in team_sixes_dict:
                            team_sixes_dict[teams] = [int(numberof6s)]
                        else:
                            team_sixes_dict[teams].append(int(numberof6s))
                        team_frequency_dict[teams] = team_frequency_dict.get(teams, 0)+1
                    except ValueError:
                        print("Unable to convert numberof6s", numberof6s)
            except ValueError:
                print("Line is not in a correct format...", line)
    except FileNotFoundError:
        print("File is not available...")
    while True:
        print("\n**********************************")
        print("\t\t\tWelcome! Main Menu")
        print("**********************************")
        print("\nPress 1 for Numerical analysis...\nPress 2 for categorical analysis...\nPress q quit...")
        menu_1 = input("Enter the valid number to process: ")
        if menu_1 == "q":
            print("\n*********************************")
            print("You are exited...Thank You!")
            print("*********************************")
            break
        elif menu_1 == "1":
            #print(runs_list)
            Numerical_stats(runs_list, highscores_list)
        elif menu_1 == "2":
            Categorical_stats(team_sixes_dict, team_frequency_dict)
        else:
            print("Invalid input... Please give valid input!")



