from .models import Image, User
from django.http import JsonResponse, HttpResponseRedirect
import boto3
import uuid

S3_BASE_URL='.s3-us-west-2.amazonaws.com'
BUCKET='photo-repository-challenge'


# Create your views here.
def add_image(request):
    image_file = request.FILES.get('image-file',None)
    if image_file:
        s3 = boto3.client('s3')
        key=uuid.uuid4().hex[:6] + image_file.name[image_file.name.rfind('.'):]

        try:
            s3.upload_fileobj(image_file, BUCKET, key)
            url=f'https://{BUCKET}{S3_BASE_URL}/{key}'
            if request.POST['title']:
                img_title = request.POST['title']
            else:
                img_title = 'Unkown'
            if request.POST['creator']:
                img_creator = request.POST['creator']
            else:
                img_creator = 'Unkown'
            image = Image(url=url,title=img_title, creator=img_creator)
            image.save()
            new_image={
              'id': image.id,
              'title':image.title,
              'creator':image.creator,
              'url':image.url,
            }
            # return JsonResponse(new_image)
            return HttpResponseRedirect('https://image-repository-challenge.netlify.app/gallery')
        except Exception as err:
            print('An error has occured uploading file to S3')
            print(err)
            return JsonResponse({'error': err})


def add_user_image(request, user_id):
    image_file = request.FILES.get('image-file',None)
    if image_file:
        s3 = boto3.client('s3')
        key=uuid.uuid4().hex[:6] + image_file.name[image_file.name.rfind('.'):]

        try:
            s3.upload_fileobj(image_file, BUCKET, key)
            url=f'https://{BUCKET}{S3_BASE_URL}/{key}'
            if request.POST['title']:
                img_title = request.POST['title']
            else:
                img_title = 'Unkown'
            if request.POST['creator']:
                img_creator = request.POST['creator']
            else:
                img_creator = 'Unkown'
            image = Image(url=url,title=img_title, creator=img_creator)
            image.save()
            if User.objects.filter(uid=user_id).exists():
              usr = User.objects.get(uid=user_id)
              usr.images.add(image)
              usr.save()
            else:
              usr = User(uid=user_id)
              usr.save()
              usr.images.add(image)
              usr.save()

            new_image={
              'id': image.id,
              'title':image.title,
              'creator':image.creator,
              'url':image.url,
            }
            # return JsonResponse(new_image)
            return HttpResponseRedirect('https://image-repository-challenge.netlify.app/gallery')
        except Exception as err:
            print('An error has occured uploading file to S3')
            print(err)
            return JsonResponse({'error': err})    


def get_user_images(request, user_id):
    try:
        usr_imgs = list(User.objects.get(uid=user_id).images.values())
        return JsonResponse({'imgs':usr_imgs})
    except Exception as err:
        print('An error getting user images')
        print(err)
        return JsonResponse({'error': err})

def delete_user_image(request, user_id, image_id):
    try:
        User.objects.get(uid=user_id).images.get(id=image_id).delete()
        return HttpResponseRedirect('https://image-repository-challenge.netlify.app/user/gallery')
    except Exception as err:
        print('An error deleting user image')
        print(err)
        return JsonResponse({'error': err})


def get_all_images(request):
    try:
        imgs_list= list(Image.objects.all().values())
        return JsonResponse({'imgs':imgs_list})
    except Exception as err:
        print('An error has occured uploading file to S3')
        print(err)
        return JsonResponse({'error': err})

def test_data(request):
  response = {'test':'success'}
  return JsonResponse(response)