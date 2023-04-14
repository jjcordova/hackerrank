# Excersice HackerRank
# Artificial IntelligenceStatistics and Machine LearningDay 6: Multiple Linear Regression: Predicting House Prices
# https://www.hackerrank.com/challenges/computing-the-correlation/problem
# Compute the correlation

import math

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
# Enter your code here. Read input from STDIN. Print output to STDOUT


# Get the parameters:
# First Line N observatiosn
# Secon line: records M F C

n= int(input())
math_record = []
physics_record = []
chemistry_record = []
scores = []
for i in range(n):
 m, p, c = map(int, input().split())
 math_record.append(m)
 physics_record.append(p)
 chemistry_record.append(c)

coef_M_P = pearson_coef(math_record,physics_record)
coef_P_C = pearson_coef(physics_record,chemistry_record)
coef_C_M = pearson_coef(chemistry_record,math_record)

print(f'{coef_M_P:.2f}')
print(f'{coef_P_C:.2f}')
print(f'{coef_C_M:.2f}')
