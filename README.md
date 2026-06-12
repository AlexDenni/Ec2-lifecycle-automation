# Automated EC2 Lifecycle Management using AWS Lambda

## Overview

This project automates AWS EC2 instance start and stop operations using AWS Lambda, EventBridge Scheduler, SNS, IAM, and CloudWatch.

The automation helps reduce AWS infrastructure costs by automatically shutting down development or test EC2 instances during non-working hours and starting them again during business hours.

---

## AWS Services Used

* AWS Lambda
* Amazon EC2
* Amazon EventBridge Scheduler
* Amazon SNS
* AWS IAM
* Amazon CloudWatch

---

## Features

* Automated EC2 start/stop scheduling
* Tag-based EC2 filtering
* SNS email notifications
* CloudWatch logging and monitoring
* Event-driven serverless architecture
* AWS cost optimization automation

---

## Architecture

EventBridge Scheduler → AWS Lambda → EC2 Start/Stop → SNS Notifications → CloudWatch Logs

---

## Tags Used

| Key         | Value |
| ----------- | ----- |
| AutoStop    | True  |
| Environment | Dev   |

---

## Lambda Runtime

* Python 3.12
* Boto3 SDK

---

## Sample Lambda Event

```json
{
  "action": "stop"
}
```

---

## Learning Outcomes

* AWS Serverless Automation
* Infrastructure Automation
* IAM Role Management
* Event-Driven Architecture
* Cloud Monitoring
* AWS SDK Automation using Boto3

---

## Future Enhancements

* Terraform Infrastructure as Code
* Slack Notifications
* CPU Utilization Based Automation
* Multi-Region EC2 Automation
* DynamoDB Audit Logging
