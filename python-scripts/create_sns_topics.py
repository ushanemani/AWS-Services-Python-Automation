import json
import sys
import boto3

env_name = sys.argv[1]

file_name='jsons/sns_create_topics_input.json'
print("Creating SNS Topics...")
client = boto3.client('sns')

def call_sns_create_topic(client,topic):  
   response = client.create_topic(topic)
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
    topics_data = json.load(data_file)
    for topic in topics_data['topics_list']:
        call_sns_create_topic(client,topic)
replace_constants_in_json()
print("Creating SNS Topics Task Complete...")
