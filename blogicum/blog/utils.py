from django.utils import timezone


def get_published_posts(queryset=None):
    """
    Фильтрует QuerySet постов, оставляет опубликованные.
    Если queryset не передан — используется Post.objects.
    """
    from .models import Post
    qs = queryset or Post.objects
    return qs.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )
