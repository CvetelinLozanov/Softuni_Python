from django import forms
from .models import Album, Song


class SongBaseForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = '__all__'

    field_order = ['song_name', 'album', 'music_file_data']


class SongCreateForm(SongBaseForm):
    pass


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class AlbumEditForm(AlbumBaseForm):
    pass


class AlbumCreateForm(AlbumBaseForm):
    pass


class AlbumDeleteForm(AlbumBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True
