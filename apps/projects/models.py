from django.conf import settings
from django.db import models
from uuslug import uuslug
from apps.utils.models import TimedAbstractModel


class Project(TimedAbstractModel):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=200, blank=True)
    description = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    is_public = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self, start_no=2)
        super(Project, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('project_detail', (), {
            'slug': self.slug
        })


class Board(models.Model):
    title = models.CharField(max_length=50)
    project = models.ForeignKey(Project, related_name='board')
    position = models.IntegerField(blank=True, null=True, default=None)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.position is None:
            self.position = self.count_project_boards()
        super(Board, self).save(*args, **kwargs)

    def count_project_boards(self):
        return Board.objects.filter(project=self.project.id).count()

    def increase_position(self):
        highest_position = self.count_project_boards() - 1
        if self.position < highest_position:
            new_position = self.position + 1
            old_position = self.position
            old_board = Board.objects.get(
                project=self.project,
                position=new_position
            )
            old_board._change_position(old_position)
            self.position = new_position
            self.save()


    def decrease_position(self):
        if self.position > 0:
            new_position = self.position - 1
            old_position = self.position
            old_board = Board.objects.get(
                project=self.project,
                position=self.position
            )
            old_board._change_position(old_position)
            self.position = new_position
            self.save()

    def _change_position(self, position):
        self.position = position
        self.save()


class Card(TimedAbstractModel):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    content = models.TextField(blank=True, null=True)
    content_markdown = models.TextField()
    project = models.ForeignKey(Project, related_name='card')
    board = models.ForeignKey(Board)
    due_date = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)
    done = models.BooleanField(default=False)

    class Admin:
        fields = (
            (None, {'fields': (
                'title', 'created', 'content_markdown', 'project', 'board', 'due_date')
            }),)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        import markdown
        self.slug = uuslug(self.title, instance=self, start_no=2)
        self.content = markdown.markdown(self.content_markdown)
        super(Card, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('card_detail', (), {
            'project_slug':self.project.slug,
            'slug': self.slug
        })


class ProjectComment(TimedAbstractModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='projectcomment_author')
    project = models.ForeignKey(Project, related_name='projectcomment_project')
    content = models.TextField(blank=True, null=True)
    content_markdown = models.TextField()

    def __unicode__(self):
        return self.content

    def save(self, *args, **kwargs):
        import markdown
        self.content = markdown.markdown(self.content_markdown)
        super(ProjectComment, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('project_comment_list', (), {
            'slug':self.project.slug
        })


class CardComment(TimedAbstractModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='cardcomment_author')
    project = models.ForeignKey(Project, related_name='cardcomment_project')
    card = models.ForeignKey(Card, related_name='cardcomment_card')
    content = models.TextField(blank=True, null=True)
    content_markdown = models.TextField()

    def __unicode__(self):
        return self.content

    def save(self, *args, **kwargs):
        import markdown
        self.content = markdown.markdown(self.content_markdown)
        super(CardComment, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('card_comment_list', (), {
            'project_slug': self.project.slug,
            'slug': self.card.slug
        })
