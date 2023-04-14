# Excersice HackerRank
# Artificial IntelligenceStatistics and Machine LearningCorrelation and Regression Lines - A Quick Recap #1
# https://www.hackerrank.com/challenges/correlation-and-regression-lines-6/problem
# Correlation Regression

import math
from sys import stdin, stdout

def pearson_coef(A,B):
  n = float(len(A))
  meanA = sum(A)/n
  meanB = sum(B)/n
  diff_meanA = map(lambda a : a - meanA, A)
  diff_meanB = map(lambda b : b - meanB, B)
  stdA = math.sqrt((1/(n-1))*sum([c*c for c in diff_meanA]))
  stdB = math.sqrt((1/(n-1))*sum([c*c for c in diff_meanB]))
  p_coef = ( sum(A[i]*B[i] for i in range(int(n))) - n*meanA*meanB )/((n-1)*stdA*stdB) 
  return(p_coef)

A = list(map(float, stdin.readline().strip().split()))
B = list(map(float, stdin.readline().strip().split()))
print(f'{pearson_coef(A,B):.3f}')