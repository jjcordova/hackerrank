# Excersice HackerRank
# Artificial IntelligenceStatistics and Machine LearningDay 6: Multiple Linear Regression: Predicting House Prices
# https://www.hackerrank.com/challenges/stat-warmup/problem
# Basic Statistics Warmup

#!/bin/python3

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def median(values):
    n=len(values)
    m = int((n+1)/2 - 1)
    values.sort()
    if n%2==1:
        med=values[m]
    else:
        med=sum(values[int((n/2)-1): int((n/2)+1) ])/2
    return(med)

def mean(values):
  n=len(values)
  m=sum(values)/n
  return m

def moda(values):
  moda_count = 1
  d_m = {}
  for v in values:
    m_v = values.count(v)
    if m_v >= moda_count:
      moda_count = m_v
      d_m.update({v:moda_count})
  max_m = max(d_m.values())
  # remove values that not max
  moda_m = { key:value for (key, value) in d_m.items() if value == max_m }
  # If more than one such value exists, print the numerically smallest one.
  min_m = min(moda_m.keys())
  return min_m   

def std_calc(values):
  n = len(values)
  m = mean(values)
  dist_mean = [ (x-m)**2 for x in values ]
  std_value=math.sqrt(sum(dist_mean)/(n))
  return std_value

def confidence95(values):
  z = 1.96
  n = len(values)
  m = mean(values)
  c = z * std_calc(values)/math.sqrt(n)
  return m-c, m+c
  #STDIN
  
n =  input()
values = list(map(float, input().split()))

print (f"{mean(values):.1f}")
print (f"{median(values):.1f}")
print (f"{moda(values):.0f}")
print (f"{std_calc(values):.1f}")
c_s, c_h  = confidence95(values)

print (f"{c_s:.1f} {c_h:.1f}")