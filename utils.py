import random
import math
import matplotlib.pyplot as plt


def get_random_color():
    letters = '0123456789ABCDEF'
    color = '#'
    for _ in range(6): color += letters[random.randint(0, 15)]
    return color
  
def two_dim_distanceFn(point1: list[int, int], point2: list[int, int], max_y):
  dist_x, dist_y = (point1[0] - point2[0]) * max_y / 5, point1[1] - point2[1]
  return round(math.sqrt(dist_x ** 2 + dist_y ** 2), 2)

def generate_random_points(max_y, points_count):
  return [[round(random.uniform(0,5), 2), round(random.uniform(0, max_y), 2)] for _ in range(points_count)]

def draw_clusters(clusters, colors, centroids, final=False):
  for i in range(len(clusters)):
   plt.scatter([point[0] for point in clusters[i]], [point[1] for point in clusters[i]], c=[colors[i] for _ in range(len(clusters[i]))], s=50)
   plt.scatter(centroids[i][0], centroids[i][1], c=colors[i], s=200)
  
  plt.xlabel("Rating")
  plt.ylabel("Downloads")
  plt.show(block=final)
  
  if not final:
    plt.pause(2)
    plt.close()