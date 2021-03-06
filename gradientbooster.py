import numpy as np
import seaborn as sns
from sklearn import svm
import time
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import KFold
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.feature_selection import RFECV
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score,confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2


def gradient_booster(data, target):

	data = data[:,2:]
	data[:,-1] = 1
	data = data.astype(float)

	x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42)
	select_feature = SelectKBest(chi2, k=10).fit(data, target)

	for i, v in enumerate(select_feature.scores_):

		print("i: ", i, 'Score list:', v)
	
	#print('Feature list:', npdata.columns)

	x_train_2 = select_feature.transform(x_train)
	x_test_2 = select_feature.transform(x_test)
	clf_rf_2 = GradientBoostingClassifier(n_estimators=150, learning_rate=0.5, max_depth=1, random_state=0)
	clr_rf_2 = clf_rf_2.fit(x_train_2,y_train)
	ac_2 = accuracy_score(y_test,clf_rf_2.predict(x_test_2))
	print('Accuracy for 20% test data with top 10 features is: ',ac_2)

	tn, fp, fn, tp = confusion_matrix(y_test, clf_rf_2.predict(x_test_2)).ravel()

	print("tn: ", tn, "fp: ", fp, "fn: ", fn, "tp: ", tp)

	cm_2 = confusion_matrix(y_test,clf_rf_2.predict(x_test_2))
	sns.heatmap(cm_2,annot=True,fmt="d", cmap="Blues")
	plt.show()

	#data = np.concatenate((data[:i], data[i+10:]), axis = 0)

	data_red = np.delete(data, 25, 1)
	data_red = np.delete(data_red, 22, 1)
	data_red = np.delete(data_red, 21, 1)

	#model= GradientBoostingClassifier(n_estimators=200, learning_rate=0.5, max_depth=1, random_state=0)
	#rfecv = RFECV(estimator=model, step=1, cv=10,scoring='accuracy')   #5-fold cross-validation
	#rfecv = rfecv.fit(data, target)

	#plt.figure()
	#plt.xlabel("Number of features selected")
	#plt.ylabel("Cross validation score of number of selected features")
	#plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
	#plt.show()

	#data_norm = (data - data.mean()) / (data.std()) 
	model= GradientBoostingClassifier(n_estimators=150, learning_rate=0.5, max_depth=1, random_state=0)
	#model.fit(data_norm, target)
	#train_error = model.score(data, target)
	#print("train_Error: ", train_error)
	scores = cross_val_score(model, data[:, 0:5], target, cv=10)
    	#devArr.append(100-scores.mean())
	print("Gradient Booster Cross validation Accuracy for first 5 features: %0.2f (+/- %0.2f) for n_estimators " % (scores.mean(), scores.std() * 2))	

	

	#for i in range(150, 400, 50):

	x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=0)
	#normalization
	x_train_N = (x_train-x_train.mean())/(x_train.max()-x_train.min())
	x_test_N = (x_test-x_test.mean())/(x_test.max()-x_test.min())

	model= GradientBoostingClassifier(n_estimators=150, learning_rate=0.5, max_depth=1, random_state=0)
	model.fit(x_train_N, y_train)
	test_score = model.score(x_test_N, y_test)
	#print("test_Error: ", (1-test_error)*100)
	print("test score for raw features with 20% test data: ", test_score)
	#model.score()

	y_pred = model.predict(x_test_N)

	cm = confusion_matrix(y_test, y_pred) 

	print("confusion matrix: ", cm)

	tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

	print("tn: ", tn, "fp: ", fp, "fn: ", fn, "tp: ", tp)

	#ac = accuracy_score(y_test,clf_rf.predict(x_test))
	#print('Accuracy is: ',ac)
	#cm = confusion_matrix(y_test,clf_rf.predict(x_test))
	#sns.heatmap(cm,annot=True,fmt="d")

	model= GradientBoostingClassifier(n_estimators=150, learning_rate=0.5, max_depth=1, random_state=0)
	model.fit(data, target)
	train_error = model.score(data, target)
	print("train_Error: ", train_error)
	scores = cross_val_score(model, data, target, cv=10)
    	#devArr.append(100-scores.mean())
	print("Gradient Booster Accuracy for cross validation with 10 fold: %0.2f (+/- %0.2f) for n_estimators " % (scores.mean(), scores.std() * 2))	

	#modelgnb = GradientBoostingClassifier(n_estimators=200, learning_rate=0.5, max_depth=1, random_state=0)
	#modelgnb.fit(data[:501], target[:501])

	#y_pred = modelgnb.predict(data[501:])

	#cm = confusion_matrix(target[501:], y_pred) 

	#print("confusion matrix: ", cm)

	#tn, fp, fn, tp = confusion_matrix(target[501:], y_pred).ravel()

	#print("tn: ", tn, "fp: ", fp, "fn: ", fn, "tp: ", tp)
	
	#Predict Output
	#predicted= model.predict(x_test)

def kbestfeatures(npdata, target):

	data = npdata[:,2:]
	data[:,-1] = 1
	data = data.astype(float)

	x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42)
	select_feature = SelectKBest(chi2, k=10).fit(data, target)

	for i, v in enumerate(select_feature.scores_):

		print("i: ", i, 'Score list:', v)
	
	#print('Feature list:', npdata.columns)

	x_train_2 = select_feature.transform(x_train)
	x_test_2 = select_feature.transform(x_test)
	clf_rf_2 = RandomForestClassifier()      
	clr_rf_2 = clf_rf_2.fit(x_train_2,y_train)
	ac_2 = accuracy_score(y_test,clf_rf_2.predict(x_test_2))
	print('Accuracy is: ',ac_2)
	cm_2 = confusion_matrix(y_test,clf_rf_2.predict(x_test_2))
	#sns.heatmap(cm_2,annot=True,fmt="d")
	#plt.show()

def recfeatureelimination(data, target):

	data = data[:,2:]
	data[:,-1] = 1
	data = data.astype(float)

'''	clf_rf = RandomForestClassifier(random_state=43)      
	clr_rf = clf_rf.fit(data, target)

	train_error = clr_rf.score(data, target)
	print("train_Error: ", train_error)

	scores = cross_val_score(clr_rf, data, target, cv=10)
    	#devArr.append(100-scores.mean())
	print("RandomForest Accuracy: %0.2f (+/- %0.2f) cv %d " % (scores.mean(), scores.std() * 2, 10))	

#	x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.3, random_state=42)

	#x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.3, random_state=42)

	#random forest classifier with n_estimators=10 (default)
	clf_rf = RandomForestClassifier(random_state=43)      
	clr_rf = clf_rf.fit(x_train,y_train)

	ac = accuracy_score(y_test,clf_rf.predict(x_test))
	print('Accuracy is: ',ac)
	cm = confusion_matrix(y_test,clf_rf.predict(x_test))
	sns.heatmap(cm,annot=True,fmt="d")

	plt.show()

	clf_rf_4 = RandomForestClassifier() 
	rfecv = RFECV(estimator=clf_rf_4, step=1, cv=5,scoring='accuracy')   #5-fold cross-validation
	rfecv = rfecv.fit(data, target)

	plt.figure()
	plt.xlabel("Number of features selected")
	plt.ylabel("Cross validation score of number of selected features")
	plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
	plt.show()	'''


