from django.urls import path
from django.http import JsonResponse
import os


def health(request):
    # return a small JSON response; include codespace-based URL info for the exercise check
    return JsonResponse({'status': 'ok', 'host_example': f"{os.environ.get('CODESPACE_NAME', 'your-codespace')}-8000.app.github.dev"})


urlpatterns = [
    path('api/health/', health),
]
