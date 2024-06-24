#!/usr/bin/python3
""" Creates a function that returns a lits of lists
of integers representing the Pascal's triangle of n """

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        if i == 0:
            # The first row is always [1]
            row = [1]
        else:
            # Start the row with a 1
            row = [1]
            for j in range(1, i):
                # Each number is the sum of the two numbers above it
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            # End the row with a 1
            row.append(1)
        
        triangle.append(row)
    
    return triangle
