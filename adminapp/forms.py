from django import forms
from .models import Pages


class PagesForm(forms.ModelForm):
    class Meta:
        model = Pages
        fields = ('site', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ordering_url'] = forms.ChoiceField(label='', required=False, choices=[
                ['', '----------'],
                ['url', 'min'],
                ['-url', 'max']
            ])
        self.fields['ordering_found'] = forms.ChoiceField(label='', required=False, choices=[
                ['', '----------'],
                ['found_date_time', 'min'],
                ['-found_date_time', 'max']
            ])
        self.fields['ordering_last'] = forms.ChoiceField(label='', required=False, choices=[
                ['', '----------'],
                ['last_scan_date', 'min'],
                ['-last_scan_date', 'max']
            ])
        self.fields['site'].required = False
        # self.fields.update({
        #     'ordering': forms.ChoiceField(label='sort', required='False', choices=[
        #         ['url', 'from A-Z'],
        #         ['found_date_time', 'min date create'],
        #         ['-found_date_time', 'max date create']
        #     ])
        # })
