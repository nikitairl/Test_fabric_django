from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Client, Dispatch, Message
from .serializers import (ClientSerializer, DispatchSerializer,
                          MessageSerializer)


class DispatchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows dispatches to be viewed or edited.
    """
    queryset = Dispatch.objects.all()
    serializer_class = DispatchSerializer

    def list(self, request, *args, **kwargs) -> Response:
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None) -> Response:
        dispatch = self.get_object()
        serializer = self.get_serializer(dispatch)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def delete(self, request, pk=None) -> Response:
        dispatch = self.get_object()
        dispatch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, *args, **kwargs) -> Response:
        instance = self.get_object()
        self.perform_update(instance)
        return Response(status=status.HTTP_206_PARTIAL_CONTENT)


class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clients to be viewed or edited.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def list(self, request, *args, **kwargs) -> Response:
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None) -> Response:
        dispatch = self.get_object()
        serializer = self.get_serializer(dispatch)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def delete(self, request, pk=None) -> Response:
        dispatch = self.get_object()
        dispatch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, *args, **kwargs) -> Response:
        instance = self.get_object()
        self.perform_update(instance)
        return Response(status=status.HTTP_206_PARTIAL_CONTENT)


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def list(self, request, *args, **kwargs) -> Response:
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None) -> Response:
        dispatch = self.get_object()
        serializer = self.get_serializer(dispatch)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def delete(self, request, pk=None) -> Response:
        dispatch = self.get_object()
        dispatch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, *args, **kwargs) -> Response:
        instance = self.get_object()
        self.perform_update(instance)
        return Response(status=status.HTTP_206_PARTIAL_CONTENT)