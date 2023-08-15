from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_field

class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        birthday = data.get('birthday')
        nickname = data.get('nickname')
        if birthday:
            setattr(user, 'birthday', birthday)
        if nickname:  
            setattr(user, 'nickname', nickname)
        return super().save_user(request, user, form, commit=commit)
