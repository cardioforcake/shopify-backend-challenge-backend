from django.shortcuts import render
from .models import Image
import boto3
import uuid

S3_BASE_URL='https://s3-us-west-2.amazonaws.com'
BUCKET='photo-repository-challenge'


# Create your views here.
def add_image(request):
    image_file = request.FILES.get('image-file',None)
    if image_file:
        s3 = boto3.client('s3')
        key=uuid.uuid4().hex[:6] + image_file.name[image_file.name.rfind('.'):]

        try:
            s3.upload_fileobj(image_file, BUCKET, key)
            url=f'{S3_BASE_URL}{BUCKET}/{key}'
            image = Image(url=url,title=request.POST['title'])
            image.save()
        except Exception as err:
            print('An error has occured uploading file to S3')
            print(err)