import boto3
import uuid

comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')

#recognizer_arn = 'arn:aws:comprehend:us-east-1:851078371316:entity-recognizer/FoodRecognizer4'

print('initiating job')
response = comprehend.start_sentiment_detection_job(
    # EntityRecognizerArn=recognizer_arn,
    JobName='Sentiment-Detection-Job-Name-{}'.format(str(uuid.uuid4())),
    LanguageCode='en',
    DataAccessRoleArn='arn:aws:iam::851078371316:role/service-role/AmazonComprehendServiceRole-FoodRole',
    InputDataConfig={
        "InputFormat": 'ONE_DOC_PER_LINE',
        "S3Uri": "s3://food-recognizer-bucket/onlyReviews_utf8.txt"
    },
    OutputDataConfig={
        "S3Uri": "s3://food-recognizer-bucket/sentimentOutput/"
    }
)
print('Job started')
