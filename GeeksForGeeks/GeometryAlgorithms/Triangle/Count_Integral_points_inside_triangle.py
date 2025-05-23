# https://www.geeksforgeeks.org/count-integral-points-inside-a-triangle/

# Picks theorem --> Number of points at the boundary and num of points inside the triangle.

"""
Pick's Theorem:
A = I + (B/2) -1

A ==> Area of Polygon
B ==> Number of integral points on edges of polygon
I ==> Number of integral points inside the polygon

We can find A using usual area of tri formula given three points.

Using the above formula, we can deduce,
I = (2A - B + 2) / 2 
"""

"""
    Now dy = 0, so the condition while dy: is no longer true, and the loop stops.
    Each time we do dx % dy, the result gets smaller than dy.
    Eventually, one of these divisions will produce 0 as a remainder.
    When dy = 0, loop ends.
"""

def boundary_points(a, b):
    dx = abs(a[0] - b[0])  # x2 - x1
    dy = abs(a[1] - b[1])  # y2 - y1
  
    # Count lattice points on the line segment (a, b)
    if dx == 0: # vertical (same x points, we need y diff)
       return dy
    if dy == 0: # horizontal (same y points, we just need x diff)
       return dx 
        
    while dy: # Find GCD by looping until dy becomes 0.
      # dx will hold the final GCD value
      """
      Euclidean Algorithm:
         We start with two numbers (e.g., 15 and 9), and want to reduce them step-by-step.
         The larger number (dx) is reduced to the smaller one (dy)
         The smaller one becomes the remainder of the division (dx % dy)
      """
      new_dx = dy
      new_dy = dx % dy # We keep the remainder of dividing the bigger number by the smaller one.
      dx = new_dx
      dy = new_dy
    return dx 
      
    """(or) 
    from math import gcd
    gcd(abs(a[0] - b[0]), abs(a[1] - b[1]))
    """
def area(p, q, r):  
    # area of a rectangle given three points
    return abs(p[0]*(q[1]-r[1]) + q[0]*(r[1]-p[1]) + r[0]*(p[1]-q[1])) / 2
      
def count_lattice_points(p, q, r):
    # To count how many lattice (integer-coordinate) points lie on the straight line segment
    # between two given points a and b, including both endpoints.
    B = boundary_points(p, q) + boundary_points(q, r) + boundary_points(r, p)
    A = area(p, q, r)
    return int(A - B/2 + 1)

p = (0, 0)
q = (0, 5)
r = (5, 0)
print(count_lattice_points(p, q, r)) 
# 6
