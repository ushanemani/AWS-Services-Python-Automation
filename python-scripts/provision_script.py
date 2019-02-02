import json
import sys
import boto3
import configparser

import create_glue_databases
import create_glue_jobs
import create_glue_crawlers
import create_sns_topics

env_name = sys.argv[1]


glue_create_databases_file='glue_create_databases_input.json'
glue_create_jobs_file='glue_create_jobs_input.json'
glue_create_crawlers_file='glue_create_crawlers_input.json'
sns_create_topics_file='sns_create_topics_input.json'

config = configparser.ConfigParser()
config.read('project.properties')

aws_account_no = config['AwsEnvSection']['project.awsacctnum']

print('AWS Account Num: '+ aws_account_no)
print('Environment Name : ' + env_name)

create_glue_databases.main(glue_create_databases_file,env_name)
create_glue_crawlers.main(glue_create_crawlers_file,env_name,aws_account_no)
create_glue_jobs.main(glue_create_jobs_file,env_name,aws_account_no)
create_sns_topics.main(sns_create_topics_file,env_name)
