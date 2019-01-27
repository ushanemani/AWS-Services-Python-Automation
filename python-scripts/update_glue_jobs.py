import json
import sys
import boto3

env_name = sys.argv[1]
aws_account_no = sys.argv[2]
file_name='jsons/glue_update_jobs_input.json'
job_role_arn = 'arn:aws:iam::'+ aws_account_no +':role/AWSGlueServiceRole-' + env_name
print("Updating Jobs...")
client = boto3.client('glue')

# create  GLUE JOB using boto3 Client
def call_glue_create_job(client,job):
   job['JobUpdate']['Role']= job_role_arn
   response = client.update_job(
    JobName=job['JobName'],
    JobUpdate=job['JobUpdate']
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
print("Updating Glue Jobs Task Complete...")
