from .models import TodoModel, User
from .serializers import TodoSerializer, TodoUpdateSerialezer, UserSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class UserApiView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class TodoApiView(APIView):
    def get(self, request):
        # todos = TodoModel.objects.filter(user=request.user.id)
        todos = TodoModel.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class TodoUpdateApiView(APIView):

    def patch(self, request, pk):
        obj = TodoModel.objects.get(pk=pk)
        serializer = TodoUpdateSerialezer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class TodoIsCheckApiView(APIView):

    def get(self, request):
        print(request.user)
        objects = TodoModel.objects.filter(is_did=False, user=request.user.id)
        serializer = TodoSerializer(objects, many=True)
        return Response(serializer.data)

class TodoCheckApiView(APIView):

    def get(self, request):
        objects = TodoModel.objects.filter(is_did=True, user=request.user.id)
        serializer = TodoSerializer(objects, many=True)
        return Response(serializer.data)
    

class TodoFilterApiView(APIView):
    def get(self, request, format=None):
        created_at = request.GET.get('search')
        print(created_at)
        if created_at:
            todos = TodoModel.objects.filter(created_at=created_at)
            serializer = TodoSerializer(todos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)



# class TodoCreateApiView(generics.CreateAPIView):
#     queryset = TodoModel.objects.all()
#     serializer_class = TodoSerializer


# class TodoUpdateApiView(generics.UpdateAPIView):
#     queryset = TodoModel.objects.all()
#     serializer_class = TodoUpdateSerialezer


# class TodoListCheckView(generics.ListAPIView):
#     queryset = TodoModel.objects.filter(is_did=True)
#     serializer_class = TodoSerializer

# class TodoListIsCheckView(generics.ListAPIView):
#     queryset = TodoModel.objects.filter(is_did=False)
#     serializer_class = TodoSerializer


# class TodoFilterApiView(generics.ListAPIView):
#     queryset = TodoModel.objects.all()
#     serializer_class = TodoSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['created_at']