from rest_framework import serializers

from courses.models import Course, Level, Lesson
from users.serializers import TeacherSerializer


class LessonSerializer(serializers.ModelSerializer):
    level = serializers.PrimaryKeyRelatedField(queryset=Level.objects.all())

    class Meta:
        model = Lesson
        fields = ('level', 'id', 'title', 'description', 'video_url', 'material_url')

    def create(self, validated_data):
        return Lesson.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.description = validated_data.get('description', instance.description)
    #     return instance


class LevelSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(read_only=True, many=True)
    teacher = TeacherSerializer(read_only=True)
    #lessons_count = Lesson.objects.annotate(Count('level'))

    class Meta:
        model = Level
        fields = ('id', 'title', 'image', 'teacher', 'lessons', 'lessons_count')

    # def create(self, validated_data):
    #     lesson_data = validated_data.pop('lessons')
    #     teacher_data = validated_data.pop('teacher')
    #     teacher = Users.objects.get_or_create()
    #     Lesson.objects.create(level=level, teacher=teacher, **lesson_data)
    #
    #     return level
    #
    def update(self, instance, validated_data):
        lesson_data = validated_data.pop('lessons')
        lessons = instance.lessons

        instance.title = validated_data.get('title')
        instance.image = validated_data.get('image')
        instance.teacher = validated_data.get('teacher')
        instance.save()
        for lesson_data in lesson_data:
            lesson = lessons.pop(0)
            lesson.title = lesson_data.get('title')
            lesson.description = lesson_data.get('description')
            lesson.video_url = lesson_data.get('video_url')
            lesson.material_url = lesson_data.get('material_url')
            lesson.save()

        return instance


class LevelForCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = ('id', 'title', 'image')


class CourseSerializer(serializers.ModelSerializer):
    level = LevelForCourseSerializer(read_only=False, many=True)

    class Meta:
        model = Course
        fields = ('id', 'logo', 'color', 'title', 'description', 'level', 'levels_count')

    def update(self, instance, validated_data):
        level_data = validated_data.pop('level')
        levels = instance.level.all()
        levels = list(levels)
        instance.logo = validated_data.get('logo')
        instance.title = validated_data.get('title')
        instance.description = validated_data.get('description')
        instance.color = validated_data.get('color')
        instance.save()

        for level_data in level_data:
            level1 = levels.pop(0)
            level1.title = level_data.get('title')
            level1.teacher = level_data.get('teacher')
            level1.image = level_data.get('image')
            level1.save()
        return instance
