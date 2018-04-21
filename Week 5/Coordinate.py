# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 12:07:21 2018

@author: simpp
"""

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    def __eq__(self,other):
        # returns True if coordinates have the same x and y coordinate
        if self.getX() == other.getX() and self.getY() == other.getY():
            return True
        else:
            return False
    def __repr__(self):
        # returns a string that looks like a valid Python expression that could 
        # be used to recreate an object with the same value
        return 'Coordinate(' + str(self.x) + ',' + str(self.y) + ')'