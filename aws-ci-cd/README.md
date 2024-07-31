# AWS CDK and CI-CD

###### What is AWS CDK?

The AWS CDK is an open-source framework that you can use to manage your AWS infrastructure using code. This approach is known as  *infrastructure as code (IaC)* . By managing and provisioning your infrastructure as code, you treat your infrastructure in the same way that developers treat code. This provides many benefits, such as version control and scalability.

###### AWS CDK vs AWS CFN

The AWS CDK is tightly integrated with AWS CloudFormation. AWS CloudFormation is a fully managed service that you can use to manage and provision your infrastructure on AWS. With AWS CloudFormation, you define your infrastructure in templates and deploy them to AWS CloudFormation. The AWS CloudFormation service then provisions your infrastructure according to the configuration defined on your templates.

AWS CloudFormation templates are  *declarative* , meaning they declare the desired state or outcome of your infrastructure. Using JSON or YAML, you declare your AWS infrastructure by defining AWS *resources* and  *properties* . Resources represent the many services on AWS and properties represent your desired configuration of those services. When you deploy your template to AWS CloudFormation, your resources and their configured properties are provisioned as described on your template.

With the AWS CDK, you can manage your infrastructure  *imperatively* , using general-purpose programming languages. Instead of just defining a desired state declaratively, you can define the logic or sequence necessary to reach the desired state. For example, you can use `if` statements or conditional loops that determine how to reach a desired end state for your infrastructure.

AWS Cloud Development Kit has support for following languages:

* TypeScript
* JavaScript
* Python
* Java
* C#
* Go

##### Setting up dev env

To initiate a CDK app, run the following command:

`cdk init app --language typescript`

Make sure to setup the IAM correctly for your dev env.

After performing the aws configure, run the following command to setup the bootstrap env

`cdk bootstrap --region ca-central-1`

Once the above command is executed successfully, run the following command to create the infrastructure.

`cdk deploy`

Now, how can we automate all these steps, so that every time a commit is pushed to your github repository, the respective actions are triggered inside AWS.


# Welcome to your CDK TypeScript project

This is a blank project for CDK development with TypeScript.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

## Useful commands

* `npm run build`   compile typescript to js
* `npm run watch`   watch for changes and compile
* `npm run test`    perform the jest unit tests
* `npx cdk deploy`  deploy this stack to your default AWS account/region
* `npx cdk diff`    compare deployed stack with current state
* `npx cdk synth`   emits the synthesized CloudFormation template
