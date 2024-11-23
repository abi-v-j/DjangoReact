from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST'])
def message(request):
    print(request.data)
    return Response({"message": "This is a message view."})

