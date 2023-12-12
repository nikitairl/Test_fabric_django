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
        Args:
            request: The request object.
            pk (Optional): The primary key of the object to retrieve.
        Returns:
            A Response obj containing the serialized data of the retrieved obj.
        """
        dispatch = self.get_object()
        serializer = self.get_serializer(dispatch)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs) -> Response:
        """
        Creates a new object using the provided request data.
        Args:
            request (Request): The request object containing the data
            for creating the object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        Returns:
            Response: The response object containing the serialized data of
            the created object.
        Raises:
            ValidationError: If the provided data is invalid.
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
        Parameters:
            request: The HTTP request object.
            pk (optional): The primary key of the object to be deleted.
        Returns:
            A `Response` object with status code `204` (No Content).
        """
        dispatch = self.get_object()
        dispatch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, *args, **kwargs) -> Response:
        """
        PATCH method for updating an object.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            A Response object with a status code of 206 indicating
            that the update was partial.
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
        Parameters:
            request (Request): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        Returns:
            Response: The HTTP response object containing the serialized data.
        Raises:
            serializers.ValidationError: If the request data is invalid.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        try:
            schedule_send_message(serializer.data)
        except Exception as e:
            print(e)
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
        Parameters:
            request (Request): The request object that initiated
            the function call.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        Returns:
            Response: A Response object containing the serialized
            data of the queryset.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None) -> Response:
        """
        Retrieve a single object.
        Args:
            request (Request): The request object.
            pk (int, optional): The primary key of the object
            to retrieve. Defaults to None.
        Returns:
            Response: The response object containing the serialized
            data of the retrieved object.
        """
        dispatch = self.get_object()
        serializer = self.get_serializer(dispatch)
        return Response(serializer.data)
