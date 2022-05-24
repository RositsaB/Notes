from django import forms

from notes.web.models import Profile, Note


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'age', 'image')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image': 'Link to Profile Image',
        }


class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'image')
        labels = {
            'image': 'Link to Image'
        }


class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'image')
        labels = {
            'image': 'Link to Image'
        }


class DeleteNoteForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Note
        fields = ('title', 'content', 'image')
        labels = {
            'image': 'Link to Image'
        }
