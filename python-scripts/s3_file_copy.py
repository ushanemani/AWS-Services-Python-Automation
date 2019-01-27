import json
import sys
import boto3
import subprocess
env_name = sys.argv[1]

file_name='jsons/s3_file_copy_input.json'
print("Copying Files ...")

def copy_s3_files(file_paths): 
   cmd = 'aws s3 cp {} {} --recursive --include {}'.format(file_paths['input-path'],file_paths['s3-path'],file_paths['include-regex'] )
   result = subprocess.run(cmd, check=True, shell=True, stdout=subprocess.PIPE)
   print(result.stdout) 

      
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
    s3files_data = json.load(data_file)
    for file_paths in s3files_data['file_paths_list']:
        copy_s3_files(file_paths)
replace_constants_in_json()
print("Copying Files completed...")
