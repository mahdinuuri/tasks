from rest_framework import serializers
from .models import Opera, Members

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'

class OperaSerializer(serializers.ModelSerializer):
    members = MemberSerializer(many=True)

    class Meta:
        model = Opera
        fields = '__all__'

    def create(self, validated_data):
        members_data = validated_data.pop('members')
        opera = Opera.objects.create(**validated_data)
        
        for member_data in members_data:
            member, created = Members.objects.get_or_create(**member_data)
            opera.members.add(member)
        
        return opera

    def update(self, instance, validated_data):
        members_data = validated_data.pop('members', None)
        
        if members_data is not None:
            instance.members.clear()
            for member_data in members_data:
                member, created = Members.objects.get_or_create(**member_data)
                instance.members.add(member)
        
        instance.task = validated_data.get('task', instance.task)
        instance.duedate = validated_data.get('duedate', instance.duedate)
        instance.description = validated_data.get('description', instance.description)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.priority = validated_data.get('priority', instance.priority)
        
        instance.save()
        return instance
