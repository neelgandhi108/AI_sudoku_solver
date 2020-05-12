# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: The naked twin strategy introduces another constraint in our gameplay; this way we help our agent to get more information about the board before going to the DFS stage.  
   This way our constraint propagation becomes more powerful, avoiding some branches that we would have to go in the search stage of our algorithm.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: When we play diagonal soduku, we actually have two other units to apply our constraints. What seems to be harder, turns out to be helpful.  
   Whenever we apply our eliminate, naked_twins or only_choice we actually advance more in the puzzle, since we can remove possibilities from the diagonals as well.  
   Therefore, constraint propagation helps us determine fewer options to our solution. By reducing the possible outcomes, our search stage a lot easier and faster!

### Install

This project requires **Python 3**.

[Anaconda](https://www.continuum.io/downloads), is recommended, since it contains all of the necessary libraries and software for this project.
Please try using the environment provided in the repo.

##### Optional: Pygame
Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solution.py` - file submited to udacity...
* `solution_test.py` - some test cases...
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.
* `great_solution.py` - Same as solution, but the code was separated in three files.

#git clone:-https://github.com/neelgandhi108/AI_sudoku_solver.git
