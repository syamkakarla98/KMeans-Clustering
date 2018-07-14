# [KMeans Clustering Using Python](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)

## Brief Intro to KMeans Clustering
* [K-Means clustering](https://en.wikipedia.org/wiki/K-means_clustering) is an iterative algorithm widely used in all data analasis for       finding similarity groups in a data called _Clusters_.

* It is an **unsupervised learning** technique.

* It attempts to group individuals in a population together by similarity, but not driven by a specific purpose. 

* As you don’t have prescribed labels in the data and no class values denoting a priori grouping of the data instances are given, 
	In this Repo,let’s seeabout the famous centroid based clustering algorithm — **K-means**a — in a simplest way.

## Steps to implement KMeans Clustering

* Here we implemented k-means clustering using **sci-kit learn**.
 
   1. To run a k-means algorithm, you have to randomly initialize three points called the cluster centroids,
      because I want to group my data into three clusters. 

   2. K-means moves the centroids to the average of the points in a cluster. In other words, 
      the algorithm calculates the average of all the points in a cluster and moves the centroid to that average location.

   3. This process is repeated until there is no change in the clusters (or possibly until some other stopping condition is met).
      **K** is chosen randomly or by giving specific initial starting points by the user for finding good reslts.


* K-means is used for exploratory **data mining**, you must examine the clustering results anyways to determine which clusters make sense. The value for k can be decreased if some clusters are too small, and increased if the clusters are too broad.
      
## Example

* Importing all dependencies.

``` python
	import matplotlib.pyplot as plt
	import numpy as np
	from sklearn.datasets.samples_generator import make_blobs
	from sklearn.cluster import KMeans
```
* Creating blobs dataset.

``` python
	X, y_true = make_blobs(n_samples=300, centers=3,
                       cluster_std=.50, random_state=0)
````
* Scatter plot between two dimensions.

``` python
	plt.scatter(X[:, 0], X[:, 1], s=20);
	plt.show()
````
* Output of the data before clustering is:

	![before_clustering](https://user-images.githubusercontent.com/36328597/42724536-cde998d4-8791-11e8-96ac-7ae35591fa91.png)

* Applying **kmeans** on the dataset.

``` python
	kmeans = KMeans(n_clusters=3) 
	kmeans.fit(X)
	y_kmeans = kmeans.predict(X)
````
* Scatter plot after **k-means** clustering with centroids shown as _black circle_.

``` python
	plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=20, cmap='viridis')
	centers = kmeans.cluster_centers_
	plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);
	plt.show()
````
* The output will be:

	![after_clustering](https://user-images.githubusercontent.com/36328597/42724534-cd6d7d30-8791-11e8-926c-4bf127102658.png)


## K_Means fails ?

* _Yes_, K-Means algorithm fails for **non-linear** datasets
* The learning algorithm requires apriori specification of the number of  cluster centers.
* The use of  Exclusive Assignment - If  there are two highly overlapping data then k-means will not be able to resolve that there 	are two clusters.
* Applicable only when mean is defined i.e. fails for categorical data.
* Unable to handle noisy data and outliers.
* Let us consider the below dataset :
	
	![before_clustering_moons](https://user-images.githubusercontent.com/36328597/42724537-ce229684-8791-11e8-8007-89cb5dda1205.png)

	
* By seeing the figure, we can say that there are two clusters but this algorithm doe'n work fine.
* The below plot is after k-means on the dataset:
	
	![after_clustering_moons](https://user-images.githubusercontent.com/36328597/42724535-cdae71fa-8791-11e8-9d69-7a843263ffd0.png)



### License:

* This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/syamkakarla98/KMeans-Clustering/blob/master/LICENSE.md) file for details




