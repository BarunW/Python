import pandas as pd
import datetime as dt

mean = 0
median = 0
def lets_sort(col):
	sort(col)
	return col	
# function for calculating mean
def calMean(col):
	totalSum = 0
	tDataPoint = len(col)
	for i in range (0,len(col)):
		totalSum =  totalSum + col[i] 
		mean =  round(totalSum/tDataPoint,3)
	return mean
# function for calculating median

def calMedian(original_col):
	mid = int(len(original_col)/2)
	col = original_col
	totalDataPoint = len(col)
	sort_func = lets_sort(col)
																
	if totalDataPoint % 2 == 0: # for even
		median = (sort_func[mid] + sort_func[mid-1])/2
		return median
	if totalDataPoint % 2 != 0: # for odd
		median = sort_func[mid]
		return median

# function for variance
def variance(cols):
	func_mean = calMean(cols)
	sum_i = 0
	diff_i = 0
	tDataPoint = len(cols)
	for i in range(0, tDataPoint):
		diff_i = (cols[i] - func_mean) ** 2 # sum of (element - mean) ** 2
		sum_i += diff_i
	sampleVariance = round(sum_i / (tDataPoint -1),3) # for pouplation variation use vsum/tDatPoint
	return sampleVariance

def standardDeviation(cols):
	sVariance = variance(cols)
	standardDeviation = round(sVariance**(1/2),3)
	return standardDeviation

def summarize(data):
	mn = calMean(data)
	md = calMedian(data)
	v = variance(data)
	sD = standardDeviation(data)
	max_num = max(data)
	min_num = min(data)
	col = {'Stats':['Mean','Median','Variance','StD','Max','Min'],
			'Value':[mn,md,v,sD,max_num,min_num]}
	df = pd.DataFrame(col)
	return df
