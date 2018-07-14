# [KMeans Clustering ]

## Brief Intro on KMeans Clustering
* [K-Means clustering](https://en.wikipedia.org/wiki/K-means_clustering) is an iterative algorithm widely used in all data analasis for       finding similarity groups in a data called *_Clusters_.

* It is an **unsupervised learning** technique.

* It attempts to group individuals in a population together by similarity,but not driven by a specific purpose. 

* As you don’t have prescribed labels in the data and no class values denoting a prior grouping of the data instances are given, 
	In this Repo,let’s seeabout the famous centroid based clustering algorithm — **K-means**a — in a simplest way.

## Steps to implement

Here we implemented k-means clustering using sci-kit learn.
    
    1.To run a k-means algorithm, you have to randomly initialize three points called the cluster centroids,
      because I want to group my data into three clusters. 

    2.K-means moves the centroids to the average of the points in a cluster. In other words, 
      the algorithm calculates the average of all the points in a cluster and moves the centroid to that average location.

    3.This process is repeated until there is no change in the clusters (or possibly until some other stopping condition is met).
      **K** is chosen randomly or by giving specific initial starting points by the user for finding good reslts.

    * K-means is used for exploratory **data mining**, you must examine the clustering results anyways to determine which clusters make sense. 
      The value for k can be decreased if some clusters are too small, and increased if the clusters are too broad.
