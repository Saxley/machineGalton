import os # I use this library to get the number of elements in a directory
import numpy as np # I use the numpy library to generate random numbers in a binomial way.
import matplotlib.pyplot as plt # I use the matplotlib.pyplot library to generate the chart
from collections import Counter # Counter will help us count the repeated numbers in the acquired array
from typing import Dict # typing helps us determine what a function returns and what it receives.

def count_files_in_directory(path:str) -> int:
    """
    Counts the number of files in the folder.
    
    Receives the arguments:
        path (str): The path of the folder.

    Returns:
        int: The number of elements in the folder.
    """
    try:
        # Generates a list of all elements inside the specified folder.
        elements = os.listdir(path)
        
        # Returns the length of the list, which is the total number of elements.
        return len(elements)
    except FileNotFoundError:
        # Handles the case where the path does not exist.
        print(f"Error: The folder '{path}' was not found.")
        return -1  # Returns -1 to indicate an error



def simulate_galton_machine(num_balls: int, num_levels: int) -> Dict[int, int]:
    """
    Simulates the fall of marbles in a Galton board.
    
    Receives the arguments:
        num_balls (int): Total number of marbles.
        num_levels (int): Number of levels of the Galton board.

    Returns:
        dict: Keys = containers, Values = number of marbles in each container.
    """
    # Generates 3000 numbers, where each number is the count of times a marble 
    # deviated in the 12 levels of the Galton board.
    # Each ball has a 0.5 probability of deviating to the right at each level
    results = np.random.binomial(num_levels, 0.5, size=num_balls)

    # We count the repeated values of the 3000 elements, the 'Counter' function returns a Counter object.
    # This object is very similar to a dictionary; it is based on the number as the key and the count of that number as the value
    counts = Counter(results)
    # We make sure to return a 'dictionary' data type by transforming the Counter object into a dict
    return dict(counts)


def plot_histogram(data: Dict[int, int], filename: str) -> None:
    """
    Plots a histogram from the simulation results.
    Generates a chart in the images folder.
    
    Receives the arguments:
        data(Dict[int:int]): a dictionary with key-value pairs of integers
        filename(str): a text string that serves as a path to store the histogram
    
    Returns:
        Does not return anything
    """
    container_indices = sorted(data.keys()) # we get the indices and sort them with the 'sorted' function 
    ball_counts = [data[i] for i in container_indices] # we create a new list with values ordered according to the indices

    plt.figure(figsize=(10, 6)) # We create our plot
    ''' 
    We indicate that a bar chart will be created on the plot.
    We pass 2 values that will act as X,Y.
    We assign color to the bars and their edges.
    '''
    plt.bar(container_indices, ball_counts, color="orange", edgecolor="green") 

    plt.title("Simulation of the Galton Machine") # We assign a title to the chart
    plt.xlabel("Containers") # We assign a name to the X axis
    plt.ylabel("Number of Marbles") # We assign a name to the Y axis
    plt.xticks(container_indices) # We indicate the number of bars that will be visible
    plt.grid(axis="y", linestyle="dotted", alpha=0.7) # We draw a grid to make it look similar to the Galton board

    plt.savefig(filename, dpi=150) # We save the image with a resolution of 150
    plt.close() # we close the plot
    print(f"The histogram has been saved as '{filename}'") # We notify the creation and the name


if __name__ == "__main__":
    #CONSTANTS
    NUM_BALLS = 3000 # number of balls
    NUM_LEVELS = 12 # number of levels
    FOLDER_PATH = './images' # Storage path

    # VARIABLES
    # Calls the function that will count the elements in my images folder
    num_elements = count_files_in_directory(FOLDER_PATH) # number of files in the folder
    name_histogram = f"{FOLDER_PATH}/galton_histogram_{num_elements+1}.png" # path with the new name for the new file

    results = simulate_galton_machine(NUM_BALLS, NUM_LEVELS) # We run the simulator
    plot_histogram(results, name_histogram) # We create the chart