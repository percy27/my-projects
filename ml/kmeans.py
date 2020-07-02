from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
df = [[0.15, 0.71],[0.08, 0.9],[0.16, 0.85],[0.2, 0.3],[0.25, 0.5],[0.24, 0.1]]

clf = KMeans(n_clusters=2,init=np.array([[0.15, 0.71],[0.08, 0.9]]))
clf.fit(df)
new_centroid = clf.cluster_centers_
label = clf.labels_
test = [[0.1,0.6],[0.3, 0.2]]
print(clf.predict(test))

plt.scatter([df[i][0] for i in range(len(df))],[df[i][1] for i in range(len(df))],color='b')
plt.scatter([test[i][0] for i in range(len(test))],[test[i][1] for i in range(len(test))],color='r')