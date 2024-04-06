from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
import os

UPLOADS_DIR = 'uploads'

# Ensure 'uploads' directory exists
if not os.path.exists(UPLOADS_DIR):
    os.makedirs(UPLOADS_DIR)

@require_http_methods(["POST"])
def create_file(request):
    filename = request.POST.get('filename')
    content = request.POST.get('content')
    password = request.POST.get('password', None)

    if not (filename and content):
        return HttpResponseBadRequest("Filename and content are required.")

    # Check if filename already exists
    if os.path.exists(os.path.join(UPLOADS_DIR, filename)):
        return HttpResponseBadRequest("File with this name already exists.")

    # Save file
    with open(os.path.join(UPLOADS_DIR, filename), 'w') as file:
        file.write(content)

    return JsonResponse({"message": "File uploaded successfully."})

@require_http_methods(["GET"])
# def get_files(request):
#     files = os.listdir(UPLOADS_DIR)
#     return JsonResponse({"files": files})

def get_files(request):
    media_dir = 'uploads'
    if not os.path.exists(media_dir):
        return render(request, 'getfiles.html', {'files': []})  # Empty file list

    file_list = os.listdir(media_dir)
    return render(request, 'getfiles.html', {'files': file_list})

@require_http_methods(["GET"])
def get_file(request, filename):
    password = request.GET.get('password', None)

    if not os.path.exists(os.path.join(UPLOADS_DIR, filename)):
        return HttpResponseBadRequest("File not found.")

    # Check for password protection
    if password:
        # Handle password check logic here
        # For simplicity, let's assume password is correct if provided
        pass

    with open(os.path.join(UPLOADS_DIR, filename), 'r') as file:
        content = file.read()

    return JsonResponse({"filename": filename, "content": content})

@require_http_methods(["POST", "GET"])
def update_file(request, filename):
    if request.method == 'POST':
        content = request.POST.get('content')

        if not content:
            return HttpResponseBadRequest("Content is required.")

        if not os.path.exists(os.path.join(UPLOADS_DIR, filename)):
            return HttpResponseBadRequest("File not found.")

        with open(os.path.join(UPLOADS_DIR, filename), 'w') as file:
            file.write(content)

        return JsonResponse({"message": "File updated successfully."})
    else:
        return render(request, 'update_file.html', {'filename': filename})
@require_http_methods(["POST", "GET"])
def delete_file(request, filename):
    if request.method == 'POST':
        if not os.path.exists(os.path.join(UPLOADS_DIR, filename)):
            return HttpResponseBadRequest("File not found.")

        os.remove(os.path.join(UPLOADS_DIR, filename))

        return JsonResponse({"message": "File deleted successfully."})
    else:
        # If the request method is not POST, return a 405 Method Not Allowed response
        return HttpResponseNotAllowed(["POST"])





def home(request):
    return render(request,"form.html")

def homepage(request):
    return render(request,"Home.html")

def getdata(request):
    return render(request,"getfiles.html")

def download_file(request, filename):
    file_path = os.path.join('uploads', filename)
    if not os.path.exists(file_path):
        return HttpResponse("File not found", status=404)

    # Open the file and prepare the response for download
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response