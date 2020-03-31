import pyspark as spark
import random

def inside(p):     
  x, y = random.random(), random.random()
  return x*x + y*y < 1

num_samples = 1000000000

sc = spark.SparkContext(appName="Pi")

count = sc.parallelize(range(0, num_samples)).filter(inside).count()

pi = 4 * count / num_samples
print(pi)

