import base64
import json
import boto3
import pymysql
import os

# Initialize S3 client
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Get the image data from the event (assuming base64 encoded string)
    image_data = event['image_data']
    bucket_name = 'your-bucket-name'
    object_key = 'your-image-key.jpg'  # or generate dynamically

    try:
        # Decode the base64 image data
        image_bytes = base64.b64decode(image_data)

        # Upload to S3
        s3_client.put_object(Bucket=bucket_name, Key=object_key, Body=image_bytes)

        return {
            'statusCode': 200,
            'body': json.dumps(f'Image uploaded to {bucket_name}/{object_key}')
        }
    except Exception as e:
        print(f"Error uploading image: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error uploading image')
        }