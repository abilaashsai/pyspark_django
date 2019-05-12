from django.shortcuts import render
import os

from pyspark import SparkContext
from pyspark.sql.session import SparkSession
from django.http import HttpResponse
from django.template import loader

import json

SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))
os.path.join(os.path.join(SETTINGS_PATH, 'templates'), 'hello.html')


# sc = SparkContext("local", "first app")
# spark = SparkSession(sc)


def index(request):
    data = {}
    with open(os.path.join(os.path.join(SETTINGS_PATH, 'route'), 'sampleoutput.json')) as json_file:
        data = json.load(json_file)
    dict = data['columns']
    template = loader.get_template('templates/index.html')
    context = {
        'columns': dict,
    }
    return HttpResponse(template.render(context, request))


def home(request):
    return render(request, 'templates/hello.html', {})


def display(request):
    dff = sc.textFile('file:///Users/abilashr/Downloads/flights.csv')
    df = spark.read.csv(dff)
    pdf = df.toPandas()
    print(pdf.columns)
    print(pdf)

    return HttpResponse(pdf.to_html())
