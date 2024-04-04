from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
import re


def validate_username(value):
   if not re.match(r'^[A-z][\w@_]{2,}$', value):
      raise ValidationError("اسم المستخدم غير صالح")


def validate_password(value):
   if not re.match(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$', value):
      raise ValidationError('كلمة مرور غير صالحة')


def validate_email(value):
   EmailValidator(
       message="البريد الالكتروني غير صحيح")(value)


def validate_phone(value):
   if not re.match('^05[0-9]{4}[0-9]{4}$', value):
      raise ValidationError(
          'رقم الهاتف يجب ان يكون مكون من 10 ارقام و ان يبدأ بـ 05')


def validat(**keywords):
   for key, value in keywords.items():
      match key:
         case "username":
            validate_username(value)

         case "phone":
            validate_phone(value)

         case "email":
            validate_email(value)

         case "password":
            validate_password(value)

         case _:
            raise NotImplementedError()

      return value
