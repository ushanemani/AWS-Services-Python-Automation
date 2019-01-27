import json
import sys
import boto3

env_name = sys.argv[1]
aws_account_no = sys.argv[2]
file_name='jsons/glue_create_crawlers_input.json'
print("Creating Crawlers...")
crawler_role_arn = 'arn:aws:iam::'+ aws_account_no +':role/AWSGlueServiceRole-' + env_name
client = boto3.client('glue')

def call_glue_create_crawler(client,crawler):  
   response = client.create_crawler(
    Name=crawler['Name'],
    Description=crawler['Description'],
    Role=crawler_role_arn,
    DatabaseName=crawler['DatabaseName'],
    Targets=crawler['Targets'],
    Schedule=crawler['Schedule'],
    TablePrefix=crawler['TablePrefix'],
    SchemaChangePolicy=crawler['SchemaChangePolicy']
    )
   print(response)
   
   
# replace any variable in the given file,we are replacing env here. Add code for future.
def replace_vars_in_json():
    with open(file_name, 'r') as file :
      filedata = file.read()
      filedata = filedata.replace('{env}',env_name)
    with open(file_name, 'w') as file:
      file.write(filedata)

# replace any constant in the given file,we are replacing env here. Add code for future.
def replace_constants_in_json():
    with open(file_name, 'r') as file :
      filedata = file.read()
      filedata = filedata.replace(env_name,'{env}')
    with open(file_name, 'w') as file:
      file.write(filedata)
      
# main code to parse JSON file and create GLUE Job
replace_vars_in_json()
with open(file_name,'r') as data_file:
    crawlers_data = json.load(data_file)
    for crawler in crawlers_data['crawlers_list']:
        call_glue_create_crawler(client,crawler)
replace_constants_in_json()
print("Creating Glue Crawlers Task Complete...")
