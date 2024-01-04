"""
    Categorical statistics or Categorical visualisation is defined as function and based on the user input the respective functions are called.

    Student ID: A00315875
    Date: 20/12/2023
"""
from IPL_Stats import *
import matplotlib.pyplot as plt
def Categorical_stats(team_sixes_dict, team_frequency_dict):
    """
        To show menu, call the Categorical statistics function, Visualization function

        Parameters:
        - team_sixes_dict: dictionary.
        dictionary of team sixes

        - team_frequency_dict: dictionary.
        dictionary of team frequencies

        Returns:
        - None
            """
    print("\nYou are in Categorical Analysis:")
    while True:
        print("\n\t\t\tSub-Menu-2:\nPress 1 to calculate Categorical Statistics\nPress 2 to calculate Categorical Visualization\nPress q to Quit ")
        menu_3=input("Enter the valid input: ")
        if menu_3 == "q":
            break
        elif menu_3 == "1":
            cal_categorical_stat(team_sixes_dict, team_frequency_dict)
        elif menu_3 == "2":
            cat_visualization(team_sixes_dict, team_frequency_dict)
        else:
            print("Invalid input... Please give valid input!")
def cal_categorical_stat(team_sixes_dict, team_frequency_dict):
    """
            To calculate the Categorical Statistics with team_sixes_dict, team_frequency_dict

            Parameters:
            - team_sixes_dict: dictionary.
            dictionary of team sixes

            - team_frequency_dict: dictionary.
            dictionary of team frequencies

            Returns:
            - None
            """
    print("The number of Teams:",len(team_sixes_dict))
    highest_player=highest_players(team_frequency_dict)
    lowest_player=lowest_players(team_frequency_dict)
    print("The highest number of players per team:",highest_player,"("+str(team_frequency_dict[highest_player])+")" )
    print("The lowest number of players per team:", lowest_player,"("+str(team_frequency_dict[lowest_player])+")")
    print(f"The highest average number of sixes by team: {max_six(team_sixes_dict)}")
    print(f"The lowest average number of sixes by team: {min_six(team_sixes_dict)}")

def highest_players(team_frequency_dict):
    """
            To calculate the highest players in team_frequency_dict dictionary

            Parameters:
            - team_frequency_dict: dictionary.
            dictionary of team frequencies

            Returns:
            - highest_players_per_team
            """
    highest_players_per_team=max(team_frequency_dict, key=team_frequency_dict.get)
    return highest_players_per_team
def lowest_players(team_frequency_dict):
    """
            To calculate the least players in team_frequency_dict dictionary

            Parameters:
            - team_frequency_dict: dictionary.
            dictionary of team frequencies

            Returns:
            - lowest_players_per_team
            """
    lowest_players_per_team=min(team_frequency_dict, key=team_frequency_dict.get)

    return lowest_players_per_team

def max_six(team_sixes_dict):
    """
            To calculate the highest Sixes in team_sixes_dict dictionary

            Parameters:
            - team_sixes_dict: dictionary.
            dictionary of team sixes

            Returns:
            - result
            """
    global result
    team = ""
    max_average = 0
    for key, value in team_sixes_dict.items():
        average = sum(value)/len(value)
        if average > max_average:
            max_average = average
            team = key
            result=f"{team} ({max_average:.2f})"
    return result
def min_six(team_sixes_dict):
    """
            To calculate the minimum Sixes in team_sixes_dict dictionary

            Parameters:
            - team_sixes_dict: dictionary.
            dictionary of team sixes

            Returns:
            - result
            """
    global result
    team = ""
    min_average = None
    for key, value in team_sixes_dict.items():
        average = sum(value) / len(value)
        if min_average == None:
            min_average = average
        if average < min_average:
            min_average = average
            team = key
            result= f"{team} ({min_average:.2f})"
    return result

def cat_visualization(team_sixes_dict,team_frequency_dict):
    """
            To show the Menu for Visualization and based on the user input to call and show the respective functions.

            Parameters:
            - team_sixes_dict: dictionary.
            dictionary of team sixes

            - team_frequency_dict: dictionary.
            dictionary of team frequencies

            Returns:
            - None
            """
    while True:
        print("\n\t\t\tSub-Menu-2.1:\nPress 1 to show Pie-chart\nPress 2 to show Bar-graph\nPress 3 to show Box-plot\nPress q to Quit ")
        menu_3=input("Enter the valid input: ")
        if menu_3 == "q":
            break
        elif menu_3 == "1":
            fig, ax = plt.subplots(1, 1, figsize=(10, 10))
            fig.suptitle("Matplotlib Visualization")
            Cat_Pie(ax,team_frequency_dict)
            plt.show()
        elif menu_3 == "2":
            fig, ax = plt.subplots(1, 1, figsize=(10, 10))
            fig.suptitle("Matplotlib Visualization")
            Cat_Bar(ax,team_frequency_dict)
            plt.show()
        elif menu_3 == "3":
            fig, ax = plt.subplots(1, 1, figsize=(10, 10))
            fig.suptitle("Matplotlib Visualization")
            Cat_Box(ax,team_sixes_dict)
            plt.show()
        else:
            print("Invalid input... Please give valid input!")
def Cat_Pie(ax,team_frequency_dict):
    """
            To show the Pie-chart visualization with ax, team_frequency_dict

            Parameters:
            - team_frequency_dict: dictionary.
            dictionary of team frequencies
            - ax: AxesSubplot
            axes on which Pie-chart is created

            Returns:
            - None
            """
    ax.set_title("Pie Chart of Player-Count")
    ax.pie(team_frequency_dict.values(), labels=team_frequency_dict.keys(), autopct="%.0f%%")
def Cat_Bar(ax,team_frequency_dict):
    """
            To show the Bar-graph visualization with ax, team_frequency_dict

            Parameters:
            - team_frequency_dict: dictionary.
            dictionary of team frequencies
            - ax: AxesSubplot
            axes on which Bar-graph is created

            Returns:
            - None
            """
    ax.set_title("Bar Chart of Players-count")
    ax.set_xlabel("Team")
    ax.set_ylabel("Frequencies")
    ax.barh(list(team_frequency_dict.keys()), team_frequency_dict.values())

def Cat_Box(ax,team_sixes_dict):
    """
            To show the Box-plot visualization with ax, team_sixes_dict

            Parameters:
            - team_sixes_dict: dictionary.
            dictionary of team sixes
            - ax: AxesSubplot
            axes on which Box-plot is created

            Returns:
            - None
            """
    ax.set_title("Box Plot of Players-count")
    ax.set_xlabel("Teams")
    ax.set_ylabel("Players-count")
    ax.boxplot(list(team_sixes_dict.values()), showmeans=True, meanline=True,labels=team_sixes_dict.keys())