from django import forms

class signupform(forms.Form):
    Name=forms.CharField(
        label="Name",
        max_length=100,
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"name"})
    )
    Email=forms.CharField(
        widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"email"})
    )
    Password=forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"})
    )
    Mobile=forms.CharField(
        label="Mobile",
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"mobile"})
    )
    Address=forms.CharField(
        label="Address",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control","placeholder":"address"})
    )

    # def clean(self):
    #     cleaned_data = super().clean()
    #     data = cleaned_data['Mobile']
    #     if data == "abc":
    #         raise forms.ValidationError("mobile must be number")
    def clean_Mobile(self):
        data=self.cleaned_data.get('Mobile')
        if len(data)<6:
            raise forms.ValidationError("mobile no length must be 10")
        return data