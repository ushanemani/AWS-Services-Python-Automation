import json
import sys
import boto3

env_name = sys.argv[1]
aws_account_no = sys.argv[2]
file_name='jsons/glue_create_jobs_input.json'
job_role_arn = 'arn:aws:iam::'+ aws_account_no +':role/AWSGlueServiceRole-' + env_name
print("Creating Jobs...")
client = boto3.client('glue')

# create  GLUE JOB using boto3 Client
def call_glue_create_job(client,job):  
   response = client.create_job(
    Name=job['Name'],
    Role=job_role_arn,
    ExecutionProperty=job['ExecutionProperty'],
    Command=job['Command'],
    DefaultArguments=job['DefaultArguments'],
    Connections=job['Connections'],
    MaxRetries=job['MaxRetries'],
    MaxCapacity=job['MaxCapacity'],
    Timeout=job['Timeout']
    )
   #update_glue_job(job)
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
    jobs_data = json.load(data_file)
    for job in jobs_data['jobs_list']:
        call_glue_create_job(client,job)
replace_constants_in_json()
print("Creating Glue Jobs Task Complete...")
