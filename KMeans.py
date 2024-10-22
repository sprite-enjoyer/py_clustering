import random
import numpy as np
import matplotlib.pyplot as plt
import sys
from utils import get_random_color, two_dim_distanceFn, generate_random_points, draw_clusters

max_y, clusters_count, points_count = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

def rand_centroids(k: int, points: list[list[int, int]]):
  x_list, y_list = [point[0] for point in points], [point[1] for point in points]
  min_x, max_x, min_y, max_y = min(x_list), max(x_list), min(y_list), max(y_list)
  return [[random.uniform(min_x, max_x), random.uniform(min_y, max_y)] for _ in range(k)]

def new_centroid(cluster): 
  x_list, y_list = [point[0] for point in cluster], [point[1] for point in cluster]
  if len(x_list) != 0: return [sum(x_list)/len(x_list), sum(y_list)/len(x_list)]
  return [0, 0] 

def k_means_clustering(k, points, distanceFn, rand_centroids): 
  random_colors = [get_random_color() for _ in range(k)]
  centroids = rand_centroids(k, points)
  clusters = [[] for _ in range(k)]
  converged = False
  
  while not converged: 
    clusters = [[] for _ in range(k)]
    
    for point in points:
      distances_to_centroids = [distanceFn(point, centroid, max_y) for centroid in centroids]
      closest_cluster_index = np.argmin(distances_to_centroids)
      clusters[closest_cluster_index].append(point)
    
    draw_clusters(clusters, random_colors, centroids)
    new_centroids = [new_centroid(cluster) for cluster in clusters]
    converged = new_centroids == centroids
    centroids = new_centroids
    
  draw_clusters(clusters, random_colors, centroids, final=True)
  return clusters
  
  
points_arr = generate_random_points(max_y, points_count)
clusters_count = k_means_clustering(clusters_count, points_arr, two_dim_distanceFn, rand_centroids)




