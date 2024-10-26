import boto3
import pandas as pd

s3 = boto3.resource(
    service_name = 's3',
    region_name = 'us-east-2',
    aws_access_key_id = 'AKIAWMFUPHKJ4JCVN***',
    aws_secret_access_key = '5eZjOHONXmGgL70yNCzBhymoTJB8MjI+******'
)


# Make dataframes
foo = pd.DataFrame({'x': [1, 2, 3], 'y': ['a', 'b', 'c']})
bar = pd.DataFrame({'x': [10, 20, 30], 'y': ['aa', 'bb', 'cc']})

# Save to csv
foo.to_csv('foo.csv')
bar.to_csv('bar.csv')

# Upload files to S3 bucket
s3.Bucket('intern-task01').upload_file(Filename='foo.csv', Key='foo.csv')
s3.Bucket('intern-task01').upload_file(Filename='bar.csv', Key='bar.csv')

for obj in s3.Bucket('intern-task01').objects.all():
    print(obj)

# Load csv file directly into python
obj = s3.Bucket('intern-task01').Object('foo.csv').get()
foo = pd.read_csv(obj['Body'], index_col=0)

obj = s3.Bucket('intern-task01').Object('bar.csv').get()
foo = pd.read_csv(obj['Body'], index_col=0)
foo.head()

# Download file and read from disc
s3.Bucket('intern-task01').download_file(Key='foo.csv', Filename='foo2.csv')
pd.read_csv('foo2.csv', index_col=0)