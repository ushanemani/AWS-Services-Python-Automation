import json
import sys
import boto3
import utils
import os.path

release_type =sys.argv[1]
env_name = sys.argv[2]

file_name='jsons/'+release_type+ '/run_crawlers_input.json'

def call_glue_run_crawler(crawler,client):  
   response = client.start_crawler(
      Name=crawler
   )
   print(response)
   

# main code 

print("Running Crawlers...")
client = boto3.client('glue')
if os.path.isfile(file_name):
   utils.replace_vars_in_json(file_name,env_name)
   with open(file_name,'r') as data_file:
       crawlers_data = json.load(data_file)
       for crawler in crawlers_data['run_crawlers_list']:
          try:
              call_glue_run_crawler(crawler,client)
          except:
             print(crawler['Name'] + ' Failed to Run Crawler. ',sys.exc_info()[0])
             utils.replace_constants_in_json(file_name,env_name)
   utils.replace_constants_in_json(file_name,env_name)
   print("Running Crawlers Task Complete...")
else:
   print(file_name + ' doesnot exist. Please verify')

