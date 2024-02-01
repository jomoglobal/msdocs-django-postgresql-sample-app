### Deploy a Python (Django or Flask) web app with PostgreSQL in Azure
- Follow instructions to create a web app and database on Azure
- By the end of the tutorial, my webapp is up and running here: https://msdocs-python-postgres-xyz.azurewebsites.net/
- How to link the github actions project to my local project:
    - browse to the folder of the local git project
    - run this command to see what is linked
        - ```git remote -v```
    - run to link it to github actions project
        - ```git remote set-url origin https://github.com/jomoglobal/msdocs-django-postgresql-sample-app```

### Create a python script that fetches data to populate database
- Create a script called "fetch_azure_data.py" to fetch data from Azure API (put the script in main folder, same as "models.py")
- Modify template script: https://learn.microsoft.com/en-us/rest/api/cost-management/retail-prices/azure-retail-prices
- Modify the sript to generate different data

### Update models.py
```# restaurant_review/models.py
from django.db import models
class AzurePricing(models.Model):
    sku = models.CharField(max_length=100)
    retail_price = models.FloatField()
    unit_of_measure = models.CharField(max_length=50)
    region = models.CharField(max_length=100)
    meter = models.CharField(max_length=100)
    product_name = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.sku} - {self.product_name}"
```
### Update views.py
```from django.shortcuts import render
from .models import AzurePricing
def index(request):
    pricing_data = AzurePricing.objects.all()
    return render(request, 'restaurant_review/index.html', {'pricing_data': pricing_data})
```
### Update urls.py
```from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
]
```
### Update index.html
```{% extends "restaurant_review/base.html" %}
{% block title %}Azure Pricing List{% endblock %}

{% block content %}
  <h1>Azure Pricing</h1>

  {% if pricing_data %}
      <table class="table">
          <thead>
              <tr>
                  <th>SKU</th>
                  <th>Retail Price</th>
                  <th>Unit of Measure</th>
                  <th>Region</th>
                  <th>Meter</th>
                  <th>Product Name</th>
              </tr>
          </thead>
          <tbody>
              {% for price in pricing_data %}
                  <tr>
                      <td>{{ price.sku }}</td>
                      <td>{{ price.retail_price }}</td>
                      <td>{{ price.unit_of_measure }}</td>
                      <td>{{ price.region }}</td>
                      <td>{{ price.meter }}</td>
                      <td>{{ price.product_name }}</td>
                  </tr>
              {% endfor %}
          </tbody>
      </table>
  {% else %}
      <p>No pricing data available.</p>
  {% endif %}
{% endblock %}```