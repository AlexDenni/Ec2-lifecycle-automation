```python
import boto3
import os

# AWS Clients
ec2 = boto3.client('ec2')
sns = boto3.client('sns')

# Environment Variable
SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']


def lambda_handler(event, context):

    # Get action from event
    action = event.get('action', 'stop')

    print("Action:", action)
    print("SNS Topic ARN:", SNS_TOPIC_ARN)

    # Find EC2 instances with AutoStop=True tag
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:AutoStop',
                'Values': ['True']
            }
        ]
    )

    instance_ids = []

    # Extract Instance IDs
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])

    print("Instances Found:", instance_ids)

    # No instances found
    if not instance_ids:
        return {
            'statusCode': 200,
            'body': 'No matching instances found'
        }

    # Stop Instances
    if action == 'stop':
        ec2.stop_instances(InstanceIds=instance_ids)
        message = f"Stopped instances: {instance_ids}"

    # Start Instances
    elif action == 'start':
        ec2.start_instances(InstanceIds=instance_ids)
        message = f"Started instances: {instance_ids}"

    else:
        return {
            'statusCode': 400,
            'body': 'Invalid action'
        }

    print("Sending SNS notification...")

    # Send SNS Notification
    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject='EC2 Automation Alert',
        Message=message
    )

    print("SNS notification sent successfully")

    return {
        'statusCode': 200,
        'body': message
    }
```
