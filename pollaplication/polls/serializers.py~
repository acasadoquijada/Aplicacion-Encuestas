from rest_framework import serializers
from .models import Question, Choice


class QuestionSerializer(serializers.Serializer):
    question_text = serializers.CharField(max_length=200)
    pub_date = serializers.DateTimeField('%Y-%m-%d')

    def create(self, validated_data):
        """
        Crea y vevuelve una encuesta (sin opciones)
        """
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Actualiza y devuelve una encuesta, teniendo en cuenta los datos validados
        """
        instance.question_text = validated_data.get('question_text', instance.question_text)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.save()
        return instance

