import pandas as pd
import datetime as dt

class StatisticsBasic:
	mean = 0
	median = 0
	def lets_sort(self,col):
		for value in range(0,len(col)):
			for n_value in range(value+1,len(col)):
				if col[value] > col[n_value]:
					temp = col[n_value]
					col[n_value] = col[value]
					col[value] = temp
		return col	
	# function for calculating mean
	def calMean(self,col):
		totalSum = 0
		tDataPoint = len(col)
		for i in range (0,len(col)):
			totalSum =  totalSum + col[i] 
			mean =  round(totalSum/tDataPoint,3)
		return mean
	# function for calculating median
	def calMedian(self,original_col):
		col = original_col
		totalDataPoint = len(col)
		sort_func = self.lets_sort(col)
																	
		if totalDataPoint % 2 == 0: # for even
			mid = int(len(sort_func)/2)
			median = (sort_func[mid] + sort_func[mid-1])/2
			return median
		if totalDataPoint % 2 != 0: # for odd
			mid= int(len(sort_func)/2)
			median = sort_func[mid]
			return median
	
	# function for variance
	def variance(self,cols):
		func_mean = self.calMean(cols)
		sum_i = 0
		diff_i = 0
		tDataPoint = len(cols)
		for i in range(0, tDataPoint):
			diff_i = (cols[i] - func_mean) ** 2 # sum of (element - mean) ** 2
			sum_i += diff_i
		sampleVariance = round(sum_i / (tDataPoint -1),3) # for pouplation variation use vsum/tDatPoint
		return sampleVariance
  
	def standardDeviation(self,cols):
		sVariance = self.variance(cols)
		standardDeviation = round(sVariance**(1/2),3)
		return standardDeviation




sb = StatisticsBasic()

def mean(x):
	return sb.calMean(x)

def variance(data_set):
	return sb.variance(data_set)

def median(x):
	return sb.calMedian(x)

def standardDeviation(y):
	return sb.standardDeviation(y)

# making an summarize table 

def summarize(data):
	mn = mean(data)
	md = median(data)
	v = variance(data)
	sD = standardDeviation(data)
	max_num = max(data)
	min_num = min(data)
	col = {'Stats':['Mean','Median','Variance','StD','Max','Min'],
			'Value':[mn,md,v,sD,max_num,min_num]}
	df = pd.DataFrame(col)
	return df











