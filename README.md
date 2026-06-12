# AWS EC2 Lifecycle Automation using Lambda

## Project Overview

This project automates the start and stop operations of AWS EC2 instances using a fully serverless and event-driven architecture.

The system is designed to optimize AWS infrastructure costs by automatically shutting down development or testing EC2 instances during non-working hours and starting them again during business hours.

The automation is implemented using AWS Lambda, EventBridge Scheduler, SNS, IAM, CloudWatch, and Boto3.



# Architecture

EventBridge Scheduler
        ↓
AWS Lambda
        ↓
EC2 Start/Stop Automation
        ↓
SNS Email Notifications
        ↓
CloudWatch Logs & Monitoring


# AWS Services Used

| Service               | Purpose                         |
| --------------------- | ------------------------------- |
| AWS Lambda            | Executes automation logic       |
| Amazon EC2            | Target compute instances        |
| EventBridge Scheduler | Triggers automation on schedule |
| Amazon SNS            | Sends email notifications       |
| AWS IAM               | Provides secure permissions     |
| Amazon CloudWatch     | Logs and monitoring             |
| Boto3                 | AWS SDK for Python              |



# Features

* Automated EC2 start and stop scheduling
* Tag-based EC2 instance filtering
* SNS email notifications for automation events
* CloudWatch centralized logging
* Serverless event-driven architecture
* AWS cost optimization automation
* Infrastructure operations automation using Python



# Workflow

## Stop Workflow

1. EventBridge Scheduler triggers Lambda at 7:00 PM IST
2. Lambda identifies EC2 instances using tags
3. Lambda stops matching EC2 instances
4. SNS sends email notification
5. CloudWatch stores execution logs



## Start Workflow

1. EventBridge Scheduler triggers Lambda at 9:00 AM IST
2. Lambda identifies EC2 instances using tags
3. Lambda starts matching EC2 instances
4. SNS sends email notification
5. CloudWatch stores execution logs


# EC2 Tags Used

| Key         | Value |
| ----------- | ----- |
| AutoStop    | True  |
| Environment | Dev   |



# Lambda Runtime

| Configuration | Value                 |
| ------------- | --------------------- |
| Runtime       | Python 3.12           |
| SDK           | Boto3                 |
| Trigger Type  | EventBridge Scheduler |



# Project Structure

aws-ec2-lifecycle-automation/
│
├── lambda_function.py
├── requirements.txt
├── README.md
└── screenshots/


# Sample Lambda Event

## Stop Instances

json id="dnjlwm"
{
  "action": "stop"
}


## Start Instances

json id="jlwmpo"
{
  "action": "start"
}

# Monitoring & Logging

CloudWatch is used for:

* Lambda execution logs
* Error tracking
* Automation monitoring
* Operational visibility

SNS is used for:

* Start/Stop email alerts
* Operational notifications

---

# Security Implementation

IAM roles are used to provide secure access for Lambda to:

* Start EC2 instances
* Stop EC2 instances
* Read EC2 details
* Publish SNS notifications
* Write CloudWatch logs

---

# Learning Outcomes

This project demonstrates practical experience in:

* AWS Serverless Computing
* Infrastructure Automation
* Event-Driven Architecture
* Cloud Operations
* AWS SDK Automation using Boto3
* IAM Role Management
* Monitoring & Observability
* Cloud Cost Optimization

---

# Future Enhancements

* Terraform Infrastructure as Code
* Slack / Microsoft Teams Notifications
* CPU Utilization Based Automation
* Multi-Region EC2 Automation
* DynamoDB Audit Logging
* Auto-Healing Infrastructure Automation

---

# Real-World Use Case

Organizations commonly use this type of automation to:

* Reduce unnecessary AWS costs
* Automate development environment shutdowns
* Improve operational efficiency
* Implement infrastructure scheduling policies

---

# Author

Alexyesudass S

Migration Engineer
