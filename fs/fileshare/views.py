# fileshare_app/views.py
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
import random
import string
from .models import SharedFile
import mimetypes


def index(request):
    return render(request, 'index.html')

def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        pin = generate_pin()

        # Create a new SharedFile instance
        shared_file = SharedFile(pin=pin, file=uploaded_file)
        shared_file.save()

        return JsonResponse({'status': 'success', 'pin': pin})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

def download_file(request, pin):
    shared_file = get_object_or_404(SharedFile, pin=pin)

    file_path = shared_file.file.path
    print(f"File Path: {file_path}")
    # Use mimetypes to get the content type based on the file extension
    content_type, encoding = mimetypes.guess_type(file_path)
    if content_type is None:
        content_type = 'application/octet-stream'

    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type=content_type)
        response['Content-Disposition'] = f'attachment; filename="{pin}"'
        return response

def generate_pin():
    # Generate a random 4-digit PIN
    return ''.join(random.choices(string.digits, k=4))
