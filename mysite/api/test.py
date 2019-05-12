from django.http import HttpResponse

from pyspark import SparkContext
from pyspark.sql.session import SparkSession

import pandas as pd
# sc = SparkContext("local", "first app")
# spark = SparkSession(sc)


# def hello(request):
#     print('hello')
#
#     dff = sc.textFile('file:///Users/abilashr/Downloads/wine.csv')
#     df = spark.read.csv(dff)
#     pdf = df.toPandas()
#     print('hello')
#     print(pdf.columns)
#     print(pdf)
#
#     return HttpResponse(pdf.columns)