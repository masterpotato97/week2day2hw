# Create a function that takes in a integer value 
# representing the a number of seconds
# and returns the seconds converted to hours minutes and seconds
# the output needs to be a string in following format:
# 1H 34M 12S
# 0H 0M 30S
# 24H 12M 0S
# Be sure to use Capital letters to represent H M S


def solution(secounds):
    minute = secounds//60
    sec=secounds%60    
    hour = minute//60
    minute = minute%60
    return  f"{hour}H {minute}M {sec}S"
    


