

# Create your views here.
# from django.http import JsonResponse

# def mi_vista(request):
#     # Mensaje de respuesta
#     mensaje = "¡Hola, mundo desde Django API!"
    
#     # Devolver una respuesta JSON
#     return JsonResponse({'mensaje': mensaje})
from django.shortcuts import render
from myApp.models import Band


def band_listing(request):
    """A view of all bands."""
    bands = Band.objects.all()
    return render(request, "bands/band_listing.html", {"bands": bands})

def band_detail(request, band_id):
    """A view to display details of a specific band."""
    # Lógica para obtener los detalles de la banda con el ID proporcionado
    return render(request, "bands/band_detail.html", {"band_id": band_id})

def band_search(request):
    """A view for searching bands."""
    # Lógica para la búsqueda de bandas
    return render(request, "bands/band_search.html")