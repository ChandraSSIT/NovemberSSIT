# Data testing ( API (application program interface))
# UI testing (User interface testing)

# FE (front end team)
# BE (back end team)

# Rest API (Representational State Transfer )

# web services

# CRUD => Create ,Read,update,delete
# Create New record => Post
# Read existing data => Get
# Update existing record => Put
# Patch =>
# Delete record => Delete

# what are the things we need to know to test API =>
# the method type =>Get,Post,Put,Delete
# Address or URL ,endpoint =>
# Headers => contains security information=> encrypted

# Response => Status code
# status code => 200 ,400,500
# 200 => Success response
# 400 => Client error
# 500 => Server error

# Response => Body => output => Json (Java script object notation) => key and value pair
# query parameter => in the url we will pass the data by mentioning parameter name by using ? ,in the below url for page we are passing data
# https://reqres.in/api/users?page=2
# Get =>url/endpoint , headers
#  Response will be 200 for Get

# Post =>
# for new record response code will be 201
# url/endpoint,body
# response will contain message

# update/put=> this is to update existing record
# response code => 200
# if record not exists while performing Put it will create new record

# Patch => 200
# patch is to update some portion of data/single column then we will go for patch
# url/endpoint , body

# Delete => 204 no content
# url with path or query parameter