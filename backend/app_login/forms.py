from allauth.account.forms import LoginForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Div, Field, Fieldset, HTML, Layout, Submit

class Login(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.helper = FormHelper()
        # self.helper.form_show_labels = False
        # self.helper.layout = Layout(
        #     Fieldset(
        #         '',
        #         Field('login', placeholder='Email', css_class="form-control mb-2"),
        #         Field('password', placeholder='Password', css_class="form-control mb-2"),
        #         Div(
        #             HTML('''
        #                 <span>Remember Me</span>
        #              '''),
        #             Field('remember', label='Remember Me'),
        #         ),
        #         ButtonHolder(
        #             Submit('submit', 'Login', css_class="btn btn-primary btn-lg btn-block")
        #         )
        #     )
        # )