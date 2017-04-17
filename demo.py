# This is mean to get your started
# Accelerated Computer Science @ BDFZ Spring 2017
# Assignment: Word Counting

file = open(r"gettysburg.txt", "r", encoding="utf-8-sig")

words = file.read().split()

for i in range(10):
	print (words[i])
