from rest_framework import filters, status, viewsets
from rest_framework.response import Response

from .models import Client, Dispatch, Message
from .serializers import DispatchSerializer


class DispatchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows dispatches to be viewed or edited.
    """
    queryset = Dispatch.objects.all()
    serializer_class = DispatchSerializer

    def get_queryset(self):
        queryset = Dispatch.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def delete(self, request, pk=None):
        dispatch = self.get_object(pk)
        dispatch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_update(instance)
        return Response(status=status.HTTP_206_PARTIAL_CONTENT)
