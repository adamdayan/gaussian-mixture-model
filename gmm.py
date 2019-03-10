import numpy as np
import random
import math
from sklearn.datasets import make_blobs
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt

class gaussianMixtureModel:
    def __init__(self, x_data, clusters):
        self.x_data = x_data
        self.clusters = clusters
        self.num_features = self.x_data.shape[1]

    def initialise_distributions(self, num):
        self.dist_num = num

        self.dist_list = []

        init_cov = self.cov_mat()
        init_weight = 1 / self.dist_num 
        #mean = np.multiply(np.random.random_sample((self.dist_num, self.num_features)), x_max) - x_min
        
        
        for i in range(self.dist_num):
            dist_dict = {}
            random_idx = random.randint(0, self.x_data.shape[0])
            dist_dict["mean"] = self.x_data[random_idx,:]
            dist_dict["cov"] = init_cov
            dist_dict["weight"] = init_weight
            self.dist_list.append(dist_dict)


    def gaussian(self, x, mu, sigma):
        sigma_det = linalg.det(sigma)
        base = 1 / (pow(2 * pi, float(self.num_features) / 2) * pow(sigma_det, 1.0/2.0))

        
        
    def calc_responsibilities(self):
        for numer_dist in self.dist_list:
            numer_resp = 
            denom_resp = 0
            for denom_dist in self.dist_list:
                
        

        
            
            
            
        
    def cov(self, x, y):
        xbar, ybar = x.mean(), y.mean()
        return np.sum((x - xbar) * (y - ybar)) / (len(x) - 1)

    def cov_mat(self):
        return np.array([[self.cov(self.x_data[0], self.x_data[0])
                          ,self.cov(self.x_data[0], self.x_data[1])]
                         ,[self.cov(self.x_data[1], self.x_data[0])
                           , self.cov(self.x_data[1], self.x_data[1])]])


if __name__ == "__main__":

    #make data
    x, clusters = make_blobs(400, 2, 4, 0.5)

    gmm = gaussianMixtureModel(x, clusters)

    gmm.initialise_distributions(4)
