from rest_framework import routers, serializers, viewsets
from users.models import User

from questionbox.models import Question, Answer

router = routers.DefaultRouter()

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['url', 'username', 'email', 'is_staff']
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
router.register('users', UserViewSet)

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
	user = UserSerializer(read_only = True, default = serializers.CurrentUserDefault())
	class Meta:
		model = Answer
		fields = ['url', 'question', 'body', 'user', 'is_answer', 'timestamp']
class AnswerViewSet(viewsets.ModelViewSet):
	queryset = Answer.objects.all()
	serializer_class = AnswerSerializer
router.register('answers', AnswerViewSet)

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
	answers = AnswerSerializer(many = True, required = False)
	user = UserSerializer(read_only = True, required = False, default = serializers.CurrentUserDefault())
	class Meta:
		model = Question
		fields = ['url', 'title', 'body', 'user', 'answers', 'timestamp']
class QuestionViewSet(viewsets.ModelViewSet):
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer
router.register('questions', QuestionViewSet)
