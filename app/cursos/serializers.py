from rest_framework import serializers

from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )


class CursoSerializer(serializers.ModelSerializer):
    """Nested Relationship -> bom para relacionamentos pequenos, como OneToOne"""
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    """HyperLinked Related Field -> gera um hyperlink"""
    """view-name -> por esta usando ViewSet, é preciso passar o campo avaliacao (criado automaticamente) + detail
        que são os detalhes da avaliacao (é preciso ser especificamente (detail)"""
    # avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')
    """Primary Key Related Field -> mostra somente a PK do objeto"""
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )
