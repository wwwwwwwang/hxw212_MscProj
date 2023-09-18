import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# read two excel and eva
#                | Positive Prediction | Negative Prediction
# Positive Class | True Positive (TP)  | False Negative (FN)
# Negative Class | False Positive (FP) | True Negative (TN)

# Precision = TruePositives / (TruePositives + FalsePositives)
# Recall = TruePositives / (TruePositives + FalseNegatives)
# F-Measure = (2 * Precision * Recall) / (Precision + Recall)
# def findStdName(name,df):
# 	for col in df.columns:
# 		if name in df[col]:
# 			return df[col][0]
# 	return name

def precision(tp,fp):
	prc = tp/(tp+fp)
	return prc

def recall(tp,fn):
	rec = tp/(tp+fn)
	return rec

def f_score(pre,rec):
	fs = 2*pre*rec/(pre+rec)
	return fs

def main(loo,drp,trueArr):
	# read similar rsRx excel
	# sameRsrxDf = pd.read_excel('./rsrx.xlsx')
	# sameDisease = pd.read_excel('./disease.xlsx')
	loo = str(loo)
	drp = str(drp)
	
	# preArr = pd.read_excel("./vali_100_" + loo+"_" + drp + ".xlsx").values
	preArr = pd.read_excel('./vali_100_50_0.1.xlsx').values
	tp = 0
	fn = 0 
	fp = 0
	for r in range(0,25):
		for c in range(1,16):
			tr = trueArr[r][c]
			pr = preArr[r][c]
			if tr == pr:
				tp  =tp + 1
			elif pd.isna(tr) and pd.isna(pr) == False:
				fp = fp + 1
			elif pd.isna(tr)==False and pd.isna(pr):
				fn = fn + 1
	pre = precision(tp,fp)
	rec = recall(tp,fn)
	fs = f_score(pre,rec)
	print("numloop: "+loo+ " drop:" + drp)
	print("precision:"+str(pre))
	print("recall:"+str(rec))
	print("f-score:"+str(fs))
	return pre,rec,fs

if __name__ == '__main__':
	trueArr = pd.read_excel('./valiTrue.xlsx').values
	main(1,1,trueArr)
	# p = np.zeros((3,3))
	# r = np.zeros((3,3))
	# f = np.zeros((3,3))
	# m = 0
	# n = 0
	# for i in [10, 20,30]:
	# 	m = 0
	# 	for j in [0.1,0.2,0.3]:
	# 		pre,rec,fs =main(i,j,trueArr)
	# 		p[m][n] = pre
	# 		f[m][n] = fs
	# 		r[m][n] = rec
	# 		m = m+1
	# 	n = n+1
	# p = pd.DataFrame(p)
	# x=['10','20','30']
	# y = ['0.1','0.2','0.3']
	# plt.figure()
	# pfig = sns.heatmap(p, vmin=0, vmax=1, xticklabels = x,yticklabels = y)
	# pf = pfig.get_figure()
	# pf.savefig('./precision.png')
	# plt.figure()
	# f = pd.DataFrame(f)
	# ffig = sns.heatmap(f, vmin=0, vmax=1, xticklabels = x,yticklabels = y)
	# ff = ffig.get_figure()
	# ff.savefig('./fscore.png')
	# plt.figure()
	# r = pd.DataFrame(r)
	# rfig = sns.heatmap(r, vmin=0, vmax=1, xticklabels = x,yticklabels = y)
	# rf = rfig.get_figure()
	# rf.savefig('./recall.png')


	