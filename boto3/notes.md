1. We have two options:
    a. client = boto3.client('s3)
    b. resource = boto3.resource('s3')

2. for all new aws service, resource will not be there. So, resource will get obsolete. so use client 

3. there is a botocore where it has defined few exceptions

4. major use of boto3 is lambda functions like
    a. serverless prog like lambda functions, cost optimi, monitoring

5. we learn 
    a. lambda
    b. cost omptimisation

6. there are multiple use case for lambda function like:
    a. cloud cost optimisation- it can be triggered s3, cloud watch - event driven actions
        

7. Lambda means Compute and Serverless. and ec2 is compute
