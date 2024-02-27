from django.shortcuts import render

def webcam_stream(request):
    return render(request, 'webcamApp/webcam_stream.html')