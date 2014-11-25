Design Doc
===========

We will program in Python for our project. 

We create classes for:
- creating lists of lists (matrices) representing the grid, the basis for keeping track of the routes we have.
- creating routes. We try to find a route from a to b with as few lines as possible. We evade the other logical gates.
- drawing the matrices and routes in a graphic interface
- in main we let all the classes work together.
- a class creating a matrix representing all the conflicts (intersections) we have at a specific moment.

How will we achieve our goal:
- create the matrices with entries representing the corners of the grid. Here we will include the logical gates as negative numbers (-1 - indexed), which we import from a seperate file.
- import the gates we are supposed to connect.
- find a route from gate a to gate b using Manhattan Distance, ignoring intersections for now.
- evaluate the intersections we have so far:
	- which line has the most intersections?
	- do we have multiple lines that all intersect each other?
	- are the lines that cross multiple/a lot of lines connecting gates on the outside of the grid?
- 
-
- Hill Climber, Simulated Annealing, A*, 

To considerate:
- shall we implement the old version of the problem or the new one?
- how can we improve the visualization?
- are there other algorithms we can use to improve the result?

