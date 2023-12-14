from django.http import HttpResponseRedirect
from rest_framework import status, viewsets
from rest_framework.response import Response

from .tasks import schedule_send_message

from .models import Client, Dispatch, Message
from .serializers import (ClientSerializer, DispatchSerializer,
                          MessageSerializer)
from .permissions import IsAuthenticatedOrReadOnly


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs) -> Response:
        """
        Retrieve a list of objects.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None) -> Response:
        """
        Retrieves an object and returns its serialized data.
        """
        dispatch = self.get_object()
        serializer = self.get_serializer(dispatch)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs) -> Response:
        """
        Creates a new object using the provided request data.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def delete(self, request, pk=None) -> Response:
        """
        Deletes an object using the provided `pk` (primary key).
        """
        dispatch = self.get_object()
        dispatch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, *args, **kwargs) -> Response:
        """
        PATCH method for updating an object.
        """
        instance = self.get_object()
        self.perform_update(instance)
        return Response(status=status.HTTP_206_PARTIAL_CONTENT)


class DispatchViewSet(BaseViewSet):
    """
    API endpoint that allows dispatches to be viewed or edited.
    """
    queryset = Dispatch.objects.all()
    serializer_class = DispatchSerializer

    def create(self, request, *args, **kwargs) -> Response:
        """
        Create a new object using the provided request data.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        schedule_send_message(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class ClientViewSet(BaseViewSet):
    """
    API endpoint that allows clients to be viewed or edited.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def list(self, request, *args, **kwargs) -> Response:
        """
        Returns a Response object containing the serialized data of a queryset.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None) -> Response:
        """
        Retrieve a single object.
        """
        dispatch = self.get_object()
        serializer = self.get_serializer(dispatch)
        return Response(serializer.data)


def login_redirect(request) -> HttpResponseRedirect:
    return HttpResponseRedirect('/login/auth0')
