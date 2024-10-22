import random
from utils import two_dim_distanceFn, get_random_color, draw_clusters, generate_random_points
import sys

max_y, clusters_count, points_count = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

def k_medoids_clustering(k, points, distanceFn):
    random_colors = [get_random_color() for _ in range(k)]
    medoids = random.sample(points, k)
    clusters = [[] for _ in range(k)]
    converged = False
    
    while not converged:
        clusters = [[] for _ in range(k)]
        for i in range(len(points)):
            distances_to_medoids = [distanceFn(points[i], medoid, max_y) for medoid in medoids]
            min_val_index = distances_to_medoids.index(min(distances_to_medoids))
            clusters[min_val_index].append(points[i])
        draw_clusters(clusters, random_colors, medoids)
        new_medoids = []
        for i in range(len(clusters)):
            avg_dist_arr = []
            for j in range(len(clusters[i])):
                avg_dist = sum([distanceFn(clusters[i][j], point2, max_y) for point2 in clusters[i]])/len(clusters[i])
                avg_dist_arr.append(avg_dist)
                
            new_medoid_index = avg_dist_arr.index(min(avg_dist_arr))
            new_medoids.append(clusters[i][new_medoid_index])
            converged = new_medoids == medoids
            medoids = new_medoids
    draw_clusters(clusters, random_colors, medoids, final=True)
        
  
points_arr = generate_random_points(max_y, points_count)
clusters_count = k_medoids_clustering(clusters_count, points_arr, two_dim_distanceFn)




