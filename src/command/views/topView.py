from rest_framework import status, views
from rest_framework.response import Response

class TopView(views.APIView):

    def get(self, request, *args, **kwargs):

        return Response({'message' : 'HelloWorld'}, status.HTTP_200_OK)