from rest_framework import generics
from .models import Members
from .models import Opera
from .serializers import MemberSerializer , OperaSerializer


class MemberDetail(generics.RetrieveAPIView):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer

class MemberCreate(generics.CreateAPIView):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer

class MemberUpdate(generics.UpdateAPIView):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer

class MemberDelete(generics.DestroyAPIView):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer

class OperaDetail(generics.RetrieveAPIView):
    queryset = Opera.objects.all()
    serializer_class = OperaSerializer

class OperaCreate(generics.CreateAPIView):
    queryset = Opera.objects.all()
    serializer_class = OperaSerializer

class OperaUpdate(generics.UpdateAPIView):
    queryset = Opera.objects.all()
    serializer_class = OperaSerializer

class OperaDelete(generics.DestroyAPIView):
    queryset = Opera.objects.all()
    serializer_class = OperaSerializer

class OperaDetail(generics.RetrieveAPIView):
    queryset = Opera.objects.all()
    serializer_class = OperaSerializer

class OperaCreate(generics.CreateAPIView):
    queryset = Opera.objects.all()
    serializer_class = OperaSerializer

class OperaUpdate(generics.UpdateAPIView):
    queryset = Opera.objects.all()
    serializer_class = OperaSerializer

class OperaDelete(generics.DestroyAPIView):
    queryset = Opera.objects.all()
    serializer_class = OperaSerializer
