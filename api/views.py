from functools import partial
from django.http import Http404
from rest_framework import views, status
from rest_framework.response import Response

from .serializers import PlayerSerializer
from .models import Player

class PlayerView(views.APIView):
    """
        List all Players, or create a new one.
    """
    def get(self, request):
        data = Player.objects.all()
        serializer = PlayerSerializer(data, many=True)

        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self, request):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

class PlayerDetailView(views.APIView):
    """
        Retrive, update or delete a Player instance.
    """
    def get_object(self, pk):
        try:
            return Player.objects.get(pk=pk)
        except Player.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        player = self.get_object(pk)
        serializer = PlayerSerializer(player)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def patch(self, request, pk):
        player = self.get_object(pk)
        if 'margin' in request.data:
            odds = getattr(player, 'odds')
            old_margin = getattr(player, 'margin')
            
            if request.data['margin'] != old_margin:
                try:
                    margin = request.data['margin']
                    final_odds = odds / (1 + margin)
                    request.data['odds'] = final_odds
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data=request.data)

        serializer = PlayerSerializer(player, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def delete(self, request, pk):
        player = self.get_object(pk)
        player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
