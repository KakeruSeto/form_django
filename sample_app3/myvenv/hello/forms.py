from django import forms

class HelloForm(forms.Form):
    your_name = forms.CharField(
        label='名前',
        max_length=20,
        required=True,
        widget=forms.TextInput()
    )
    your_place =forms.CharField(
        label='場所',
        max_length=20,
        required=True,
        widget=forms.TextInput()
    )


PREFECTURE＿CHOICES=(
    ('tokyo','東京都'),
    ('kanagawa','神奈川県'),
    ('tiba','千葉県'),
    ('saitama','埼玉県'),
)

TYPE_CHOICES = (
    ('ittou', '一棟物'),
    ('kubun', '区分')
)

class SampleForm(forms.Form):
    income = forms.IntegerField(
        label='年収',
        min_value=0,
        max_value=10000000000000,
        required=True,
    )

    old1 = forms.IntegerField(
        label='築年1',
        min_value=0,
        max_value=100,
        required=True,
    )

    old2 = forms.IntegerField(
        label='築年2',
        min_value=0,
        max_value=100,
        required=True,
    )

    range1 = forms.IntegerField(
        label='価格範囲１',
        min_value=0,
        max_value=10000000000000,
        required=True,
    )

    range2 = forms.IntegerField(
        label='価格範囲2',
        min_value=0,
        max_value=10000000000000,
        required=True,
    )


    rate= forms.IntegerField(
        label='希望利回り',
        min_value=0,
        max_value=100,
        required=True,
    )
    

    send_message = forms.BooleanField(
        label='送信する',
        required=False,
    )

    prefecture_a = forms.ChoiceField(
        label='都道府県',
        widget=forms.SelectMultiple,
        choices=PREFECTURE＿CHOICES,
        required=True,
    )

    type_a = forms.ChoiceField(
        label='種別',
        widget=forms.SelectMultiple,
        choices=TYPE_CHOICES,
        required=True,
    )

