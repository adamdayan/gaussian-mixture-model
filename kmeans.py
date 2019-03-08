import numpy as np
import random
from sklearn.datasets import make_blobs
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt


class kMeans:
    def __init__(self, x_data, clusters):
        self.x_data = x_data
        self.clusters = clusters
        self.num_features = self.x_data.shape[1]

    def initialise_centroids(self, num):
        self.centroid_num = num
        x_max = np.amax(self.x_data, 0)
        x_min = np.amin(self.x_data, 0)
        
        self.centroids = []
        
        for i in range(num):
            centroid = np.empty(self.num_features)

            for j in range(self.num_features):
                centroid[j] = random.uniform(x_min[j], x_max[j])

            self.centroids.append(centroid)

        
    def assign_to_centroid(self):
        dist_list = [] 
        for c in self.centroids:
            dist_to_centroid = np.apply_along_axis(euclidean, 1, self.x_data, c)
            dist_list.append(dist_to_centroid)

        dist_matrix = np.vstack(tuple(dist_list))

        assignment_matrix = np.argmin(dist_matrix, 0)

        return assignment_matrix

    def update_centroids(self, assignment_matrix):
        movement = 0
        
        for num, c in enumerate(self.centroids):
            centroid_points = self.x_data[assignment_matrix == num,:]
            centroidal_mean = np.mean(centroid_points, 0)
            
            for j in range(self.num_features):
                movement += abs(c[j] - centroidal_mean[j])
                c[j] = centroidal_mean[j]

        return movement

                

    def cluster(self, num):
        movement = 1
        unready = True

        while unready == True:
            self.initialise_centroids(num)
            am = self.assign_to_centroid()
            uniques = np.unique(am)

            if len(uniques) == num:
                unready = False
            
        
        while movement != 0:
            am = self.assign_to_centroid()
            
            movement = self.update_centroids(am)


        self.final_assignments = am

    def visualise(self):
        fig, ax = plt.subplots(figsize=(5, 3))

        ax.scatter(x=self.x_data[:,0], y=self.x_data[:,1], marker='o', c='r')

        centroids_matrix = np.vstack(tuple(self.centroids))

        ax.scatter(x=centroids_matrix[:,0], y=centroids_matrix[:,1], marker='x', c='b')

        plt.show()

    
        


if __name__ == "__main__":

    #make data
    x, clusters = make_blobs(400, 2, 4, 0.9)

    km = kMeans(x, clusters)

    km.cluster(4)

    km.visualise()
    
