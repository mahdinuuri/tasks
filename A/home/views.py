from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Opera, Members
from .serializers import OperaSerializer, MemberSerializer

@api_view(['GET'])
def get_member(request, pk):
    try:
        member = Members.objects.get(pk=pk)
    except Members.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = MemberSerializer(member)
    return Response(serializer.data)

@api_view(['POST'])
def create_member(request):
    serializer = MemberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_member(request, pk):
    try:
        member = Members.objects.get(pk=pk)
    except Members.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = MemberSerializer(member, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_member(request, pk):
    try:
        member = Members.objects.get(pk=pk)
    except Members.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    member.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def opera_list(request):
    serializer = OperaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_opera(request, pk):
    try:
        opera = Opera.objects.get(pk=pk)
    except Opera.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = OperaSerializer(opera)
    return Response(serializer.data)

@api_view(['PUT'])
def update_opera(request, pk):
    try:
        opera = Opera.objects.get(pk=pk)
    except Opera.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = OperaSerializer(opera, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_opera(request, pk):
    try:
        opera = Opera.objects.get(pk=pk)
    except Opera.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    opera.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
