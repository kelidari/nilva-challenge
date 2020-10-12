from io import BytesIO

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from raham.settings import s3_client
from django.shortcuts import render,redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import Upload


def list_buckets():
    response = s3_client.list_buckets()
    buckets = []
    for bucket in response['Buckets']:
        buckets.append(bucket["Name"])
    return buckets


# def get_bucket_keys(bucket):
#     """Get a list of keys in an S3 bucket."""
#     keys = []
#     resp = s3_client.list_objects_v2(Bucket=bucket)
#     for obj in resp['Contents']:
#         keys.append(obj['Key'])
#     return keys


# def show_bucket(request):
#     bucket_name = "kelidari"
#     filename = r"C:\Users\USER\Desktop\images(3).jpg"
#     name_in_bucket = "image3.jpg"
#     s3_client.upload_file(filename, bucket_name, name_in_bucket)
#     return HttpResponse('ok')

@login_required(login_url='accounts:login')
def file_upload(request):
    if request.method == 'POST':
        image_file = request.FILES['image_file']
        bucket_name = "kelidari"
        name_in_bucket = image_file.name.replace(" ", "_")
        try:
            s3_client.upload_fileobj(Fileobj=image_file, Bucket=bucket_name, Key=name_in_bucket)
            s3_client.put_object_acl(ACL='public-read',Key=name_in_bucket, Bucket=bucket_name)
        except:
            return HttpResponse('<h1> آپلود فایل با مشکل مواجه شد! دوباره سعی کنید</h1>')
        # if message=='None':
        #     HttpResponse('Upload succeed')
        #     return render(request, 'upload.html')
        # else:
        #     return HttpResponse('Upload Failed!')
    return redirect('aws:download')


def get_bucket_keys(bucket):
    """Get a list of keys in an S3 bucket."""
    keys = []
    try:
       resp = s3_client.list_objects_v2(Bucket=bucket)
       for obj in resp['Contents']:
           keys.append(obj['Key'])
       return keys
    except :
        return HttpResponse('bucket '+bucket+' is empty ! pleas upload one')

@login_required(login_url='accounts:login')
def file_download(request):
    bucket_name = "kelidari"
    key=get_bucket_keys(bucket_name)
    # name=request.GET['name']
    # s3_client.download_file(Bucket=bucket_name, Key=name, Filename=r"C:\\Users\\USER\\Downloads\\"+name)
    return render(request, 'download.html', {'key': key})

@login_required(login_url='accounts:login')
def file_delete(request):
    httpRespose = HttpResponse()
    bucket_name = "kelidari"
    key = request.GET['key']

    try:
        s3_client.delete_object(Bucket=bucket_name, Key=key)

    except  :
        return HttpResponse('<h1>حذف فایل با مشکل مواجه شد! دوباره سعی کنید</h1>')

    return httpRespose('ok')
