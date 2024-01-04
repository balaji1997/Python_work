"""
    Numerical statistics or Numerical visualisation is defined and based on the user input the respective functions are called.

    Student ID: A00315875
    Date: 20/12/2023
"""
from math import sqrt
import matplotlib.pyplot as plt
from IPL_Stats import *
def Numerical_stats(runs_list,highscores_list):
    """
        To show menu, call the numerical statistics function twice, Visualization function and correlation function

        Parameters:
        - runs_list: list.
        List of runs

        - highscores_list: list.
        List of Highscores

        Returns:
        - None
    """
    while True:
        print("\n\t\t\tSub-Menu-1:\nPress 1 to calculate Numerical statistics\nPress 2 to calculate Visualization\nPress q to Quit ")
        menu_2=input("Enter the valid input: ")
        if menu_2 == "q":
            break
        elif menu_2 == "1":
            Calculate_Num_stats(runs_list,name="Runs Statistics")
            Calculate_Num_stats(highscores_list,name="High-score Statistics")
            print(f"\nCorrelation for numerical values: {calc_correlation(runs_list, highscores_list):.2f}")
        elif menu_2 == "2":
            Num_Visualization(runs_list,highscores_list)
        else:
            print("Invalid input... Please give valid input!")
def Calculate_Num_stats(numerical_list, name):
    """
       To print the statistical values of Numerical types and call their function

       Parameters:
       - numerical_list: list.
       List of runs or List of Highscores
       - name: String.
       Name of the parameter passed in numerical_list

       Returns:
       - None
        """
    print("\nNumerical stat function:", name)
    print("Number of numerical values:", len(numerical_list))
    print("Total of numerical values:", sum(numerical_list))
    print("Maximum of numerical values:", max(numerical_list))
    print("Minimum of numerical values:", min(numerical_list))
    print(f"Mean for numerical values: {Calc_the_mean(numerical_list):.2f}")
    print(f"Mode for numerical values: {Calc_the_mode(numerical_list):.2f}")
    print(f"Median for numerical values: {Calc_the_median(numerical_list):.2f}")
    print(f"Range for numerical values: {Calc_the_range(numerical_list):.2f}")
    print(f"Inter Quartile Range for numerical values: {Calc_the_interquartile_Range(numerical_list):.2f}")
    print(f"Standard deviation for numerical values: {Calc_Standard_Deviation(numerical_list):.2f}")
    print(f"Skewness_median for numerical values: {Calc_median_skewness(numerical_list):.2f}")
    print(f"Skewness_mode for numerical values: {Calc_mode_skewness(numerical_list):.2f}")

def Calc_the_mean(numerical_list):
    """
        To calculate the mean value of numerical_list

        Parameters:
        - numerical_list: list.
        List of runs or List of Highscores

        Returns:
        - mean
        """
    mean = sum(numerical_list) / len(numerical_list)
    #print(f"\nMean for numerical values: {mean:.2f}")
    return mean
def Calc_the_mode(numerical_list):
    """
       To calculate the mode value of numerical_list

       Parameters:
       - numerical_list: list.
       List of runs or List of Highscores

       Returns:
       - mode
       """
    sorted_list = sorted(list(set(numerical_list)))
    frequency_counts = []
    for line in sorted_list:
        frequency_counts.append(numerical_list.count(line))
    mode=sorted_list[frequency_counts.index(max(frequency_counts))]
    #print("\nMode for numerical values:",sorted_list[frequency_counts.index(max(frequency_counts))])
    return mode
def Calc_the_median(numerical_list):
    """
            To calculate the median value of numerical_list

            Parameters:
            - numerical_list: list.
            List of runs or List of Highscores

            Returns:
            - median
            """
    sorted_list = sorted(numerical_list)
    mid_index = int(len(sorted_list) / 2)
    if len(sorted_list) % 2 == 1:
        median = sorted_list[mid_index]
    else:
        median = (sorted_list[mid_index - 1] + sorted_list[mid_index]) / 2
    #print(f"\nMedian for numerical values: {median:.2f}")
    return median
def Calc_the_range(numerical_list):
    """
            To calculate the Range value of numerical_list

            Parameters:
            - numerical_list: list.
            List of runs or List of Highscores

            Returns:
            - range
            """
    range=max(numerical_list)-min(numerical_list)
    return range
def Calc_the_interquartile_Range(numerical_list):
    """
        To calculate the Inter quartile Range value of numerical_list

        Parameters:
        - numerical_list: list.
        List of runs or List of Highscores

        Returns:
        - Result
        """
    sorted_list = sorted(numerical_list)
    mid_index = int(len(sorted_list) / 2)
    if (len(sorted_list) % 2 == 1):
        lower_half = sorted_list[:mid_index]
        upper_half = sorted_list[mid_index + 1:]
    else:
        lower_half = sorted_list[:mid_index]
        upper_half = sorted_list[mid_index:]
    #print(upper_half)
    lower_half_median = Calc_the_median(lower_half)
    upper_half_median = Calc_the_median(upper_half)
    Result=upper_half_median - lower_half_median
    #print("\nInter-Quartile Range:",)
    return Result
def Calc_Standard_Deviation(numerical_list):
    """
            To calculate the Standard Deviation value of numerical_list

            Parameters:
            - numerical_list: list.
            List of runs or List of Highscores

            Returns:
            - result
            """
    x_mean=Calc_the_mean(numerical_list)
    squared_dev=[(x-x_mean)**2 for x in numerical_list]
    result=sqrt(sum(squared_dev)/(len(squared_dev)-1))
    return result
def Calc_median_skewness(numerical_list):
    """
            To calculate the Median Skewness value of numerical_list

            Parameters:
            - numerical_list: list.
            List of runs or List of Highscores

            Returns:
            - median_skewness
            """
    median_skewness=3* ((Calc_the_mean(numerical_list)-Calc_the_median(numerical_list))/Calc_Standard_Deviation(numerical_list))
    return median_skewness
def Calc_mode_skewness(numerical_list):
    """
           To calculate the Mode Skewness value of numerical_list

           Parameters:
           - numerical_list: list.
           List of runs or List of Highscores

           Returns:
           - mode_skewness
           """
    mode_skewness=(Calc_the_mean(numerical_list)-Calc_the_mode(numerical_list))/Calc_Standard_Deviation(numerical_list)
    return mode_skewness
def calc_correlation(runs_list, highscores_list):
    """
           To calculate the correlation value of runs_list, highscores_list

           Parameters:
           - runs_list: list.
           List of runs
           - highscores_list: list.
           List of Highscores

           Returns:
           - result
           """
    global result
    x_mean = Calc_the_mean(runs_list)
    y_mean = Calc_the_mean(highscores_list)
    x_y_value = 0
    x_sq_val = 0
    y_sq_val = 0
    for i in range(len(runs_list)):
        x_y_value += (runs_list[i] - x_mean) * (highscores_list[i] - y_mean)
        x_sq_val += (runs_list[i] - x_mean) ** 2
        y_sq_val += (highscores_list[i] - y_mean) ** 2
        result=(x_y_value / sqrt(x_sq_val * y_sq_val))
    return result



def Num_Visualization( runs_list, highscores_list):
    """
            To show the Menu for Visualization and based on the user input to call and show the respective functions.

            Parameters:
            - runs_list: list.
            List of runs
            - highscores_list: list.
            List of Highscores

            Returns:
            - None
            """
    print("\nYou are in Numerical_Visualization function")
    while True:
        print(
            "\n\t\t\tSub-Menu-1.2:\nPress 1 to show Histogram\nPress 2 to show Boxplot\nPress 3 to show Scatterplot\nPress q to Quit ")
        menu_3 = input("Enter the valid input: ")
        if menu_3 == "q":
            break
        elif menu_3 == "1":
            fig,ax=plt.subplots(1,2,figsize=(10,10))
            fig.suptitle("Matplotlib Visualization")
            Num_Histogram(ax,runs_list)
            Num_Histogram2(ax,highscores_list)
            plt.show()

        elif menu_3 == "2":
            fig, ax = plt.subplots(1, 2, figsize=(10, 10))
            fig.suptitle("Matplotlib Visualization")
            Num_Boxplot(ax,runs_list)
            Num_Boxplot2(ax,highscores_list)
            plt.show()

        elif menu_3 == "3":
            fig, ax = plt.subplots(1, 1, figsize=(10, 10))
            fig.suptitle("Matplotlib Visualization")
            Num_Scatter(ax,runs_list, highscores_list)
            plt.show()
        else:
            print("Invalid input... Please give valid input!")

def Num_Histogram(ax,runs_list):
    """
            To show the Histogram visualization with ax, runs_list

            Parameters:
            - runs_list: list.
            List of runs
            - ax: AxesSubplot
            axes on which Histogram is created

            Returns:
            - None
            """
    ax[0].set_title("Histogram of Runs")
    ax[0].set_xlabel("Runs")
    ax[0].set_ylabel("Frequency")
    bins = range(0, max(runs_list) + 50, 50)
    ax[0].set_xticks(bins)
    ax[0].hist(runs_list, bins, ec="black")
def Num_Histogram2(ax,highscores_list):
    """
            To show the Histogram visualization with ax, highscores_list

            Parameters:
            - highscores_list: list.
            List of Highscores
            - ax: AxesSubplot
            axes on which Histogram is created

            Returns:
            - None
            """
    ax[1].set_title("Histogram of HighScores")
    ax[1].set_xlabel("HighScores")
    ax[1].set_ylabel("Frequency")
    bins = range(0, max(highscores_list) + 10, 10)
    ax[1].set_xticks(bins)
    ax[1].hist(highscores_list, bins, ec="black")

def Num_Boxplot(ax,runs_list):
    """
            To show the Boxplot visualization with ax, runs_list

            Parameters:
            - runs_list: list.
            List of runs
            - ax: AxesSubplot
            axes on which Box-plot is created

            Returns:
            - None
            """
    ax[0].set_title("Box Plot of Runs")
    ax[0].set_ylabel("Runs")
    ax[0].boxplot(runs_list, showmeans=True, meanline=True)

def Num_Boxplot2(ax,highscores_list):
    """
            To show the Boxplot visualization with ax, highscores_list

            Parameters:
            - highscores_list: list.
            List of Highscores
            - ax: AxesSubplot
            axes on which Box-plot is created

            Returns:
            - None
            """
    ax[1].set_title("Box Plot of HighScores")
    ax[1].set_ylabel("HighScores")
    ax[1].boxplot(highscores_list, showmeans=True, meanline=True)

def Num_Scatter(ax,runs_list,highscores_list):
    """
            To show the scatter-plot visualization with ax, runs_list, highscores_list

            Parameters:
            - highscores_list: list.
            List of Highscores
            - runs_list: list.
            List of Runs
            - ax: AxesSubplot
            axes on which Scatter-plot is created

            Returns:
            - None
            """
    ax.set_title("Scatter plot for Runs and Scores")
    ax.set_xlabel("Runs")
    ax.set_ylabel("Highscores_list")
    ax.scatter(runs_list, highscores_list, marker=".")


