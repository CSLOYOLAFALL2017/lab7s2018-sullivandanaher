#Programmers: Rebecca Danaher and Kylee Sullivan
#Course: CS 151.02
#Professor Franceschi
#Date: March 23, 2018
# Lab 7

#This imports a certain file name
import os

#This is one of the three functions we have to use
def checkFile():
    filename = input( "Please enter the name of the file: " )
#if the user does not input correct file name, it loops again
    while not os.path.exists(filename):
        filename = input( "Please enter the name of the file: " )
    return filename

#This is the second function we have to use
def maxProfit( filename ):
    try:
#This allows us to open to file to read it
        file = open( filename, "r")
        max = 0
#This also allows us to figure out the greatest profit movie
        for line in file:
            releaseDate, movieName, budget, boxOffice = line.split(",")
            budget = float(budget)
            boxOffice = float(boxOffice)
            profit = boxOffice - budget
            if profit >= max:
                max = profit
                maxMovie = movieName
        print( "The movie that made the greatest profit was ", maxMovie, ". It's profit was: $", max, sep = "")
    except FileNotFoundError:
        print( "File does not exist." )

#This is the third functions we need to use
def wFile(filename):
    wFile = input( "Please enter the name of a file to write to: ")
#We need to open the files to read and write in them
    try:
        file = open( filename, "r")
        newFile = open(wFile, "w")
        for line in file:
            releaseDate, movieName, budget, boxOffice = line.split(",")
#The budget and boxoffice are float numbers
            budget = float(budget)
            boxOffice = float(boxOffice)
            profit = boxOffice - budget
            print( releaseDate, movieName, profit, file = newFile, sep = ", ")
#If input the wrong file name, it shows up as file does not exist
    except FileNotFoundError:
        print( "File does not exist." )

#This is our main function
def main():
    filename = checkFile()
    maxProfit(filename)
    wFile(filename)
#This calls the main function
main()
