import boto3
import pandas as pd

# pass region name, access and secret key.
conn = boto3.client('sqs',
                    region_name= < region_name >, aws_access_key_id = < access_key >, aws_secret_access_key = < secret_key >)

count = 0
while True:
    # pass url of sqs
    queue = conn.receive_message(QueueUrl= < SQS_URL >,
            AttributeNames = ['All'],
                             MaxNumberOfMessages = 10
    )
    messages = queue.get('Messages')
    if len(messages) == 0:
        break

    data_list = []
    for messages in messages:
        data = messages['Body']
        data_list.append(data)
        count += 1

data_dict = { < header_name >: data_list}  # pass header name of csv file
df = pd.DataFrame(data_dict)
df.to_csv( < file_name >, index = False)  # pass path and file name of csv.

print('Total number of messages : {}'.format(count))
