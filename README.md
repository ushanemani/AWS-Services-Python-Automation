1. Install AWS CLI, boto3 using pip install
python -m pip install --upgrade pip
pip install awscli
pip install boto3

1.automation of s3 file copy from some path to s3.
2. Automated creations of list of AWS services using RunDeck Jobs
1. Glue-Creations :
jobs
crawlers
databases
connections to JDBC
2. Glue- Updations :
Jobs
3. SNS-Creations
Topics



2. Commands to run the scripts:

python create_glue_jobs.py qa 123455678345
python create_glue_crawlers.py dev 123455678345
python create_glue_databases.py qa
python create_glue_connections.py ABC
python update_glue_jobs.py dev 123455678345
python create_sns_topics.py dev
python s3_file_copy.py dev