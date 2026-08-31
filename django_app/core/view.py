import socket
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.db import connection
from .models import Note


def get_server_identity():
    """Return a short identity string for the current web server."""
    hostname = socket.gethostname()
    print(hostname)
    return hostname


@require_http_methods(["GET", "POST"])
def index(request):
    """
    Main page of the HA demo.

    - Shows which backend (web1 / web2) handled *this* request.
    - Lets the user add a note that is stored in the shared PostgreSQL DB.
    - Lists all notes so you can see that data is consistent across backends.
    """
    server = get_server_identity()
    message = None

    if request.method == 'POST':
        text = request.POST.get('text', '').strip()
        author = request.POST.get('author', '').strip() or 'Anonymous'
        if text:
            Note.objects.create(
                text=text,
                author=author,
                created_on_host=server,
            )
            message = "Note saved to the shared PostgreSQL database."
            return redirect('index')   # PRG pattern

    notes = Note.objects.all()[:50]    # latest 50

    context = {
        'server': server,
        'notes': notes,
        'message': message,
        'note_count': Note.objects.count(),
    }
    return render(request, 'notes/index.html', context)


def health(request):
    """
    Simple health endpoint used by HAProxy httpchk.

    Returns 200 only if the application can reach the database.
    HAProxy will mark a backend as down if this fails repeatedly.
    """
    try:
        # Cheap connectivity check
        with connection.cursor() as cursor:
            cursor.execute('SELECT 1')
            cursor.fetchone()
        return JsonResponse({
            'status': 'ok',
            'server': get_server_identity(),
            'database': 'reachable',
        })
    except Exception as exc:
        return JsonResponse({
            'status': 'error',
            'server': get_server_identity(),
            'database': str(exc),
        }, status=503)


def server_info(request):
    """Tiny endpoint that only returns the current hostname (useful for testing)."""
    return HttpResponse(get_server_identity(), content_type='text/plain')

