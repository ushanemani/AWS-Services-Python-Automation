import json
import sys
import boto3

env_name = sys.argv[1]

file_name='jsons/glue_create_databases_input.json'
print("Creating DataBases...")
client = boto3.client('glue')

def call_glue_create_database(client,database):  
   response = client.create_database(
   DatabaseInput={
        'Name': database['DatabaseInput']['Name'],
        'Description': database['DatabaseInput']['Description']
        }
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
    databases_data = json.load(data_file)
    for database in databases_data['databases_list']:
        call_glue_create_database(client,database)
replace_constants_in_json()
print("Creating DataBases Task Complete...")
