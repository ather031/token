from rest_framework import serializers

class ChangePasswordSerializer(serializers.Serializer):
    old_password     = serializers.CharField(max_length=100, required=True)
    new_password     = serializers.CharField(max_length=100, min_length=6, required=True)
    confirm_new      = serializers.CharField(max_length=100, min_length=6, required=True)

    class Meta:
        fields = ['old_password', 'new_password', 'confirm_new']

    def validate(self, attrs):
        new = attrs.get('new_password')
        new2 = attrs.get('confirm_new')
        if new != new2:
            raise serializers.ValidationError("Password didn't match")
        return super().validate(attrs)
