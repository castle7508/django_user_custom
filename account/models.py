from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class Dept(MPTTModel):
    # parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    dept_id = models.CharField(max_length=8, primary_key=True)
    dept_name = models.CharField(max_length=255, null=False)
    parent_id = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    node_type = models.CharField(max_length=8, null=False)
    full_path = models.CharField(max_length=255, null=False)
    depth_level = models.IntegerField(null=False)
    ordinal = models.CharField(max_length=255, null=False)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['dept_id', 'ordinal']

    def __str__(self):
        return self.dept_name


class Duty(models.Model):
    duty_id = models.CharField(max_length=8, primary_key=True)
    duty_name = models.CharField(max_length=255, null=False)
    ordinal = models.CharField(max_length=255, null=False)
    create_date = models.DateField(auto_now_add=True)


class Position(models.Model):
    position_id = models.CharField(max_length=8, primary_key=True)
    position_name = models.CharField(max_length=255, null=False)
    ordinal = models.CharField(max_length=255, null=False)
    create_date = models.DateField(auto_now_add=True)


class User(AbstractBaseUser):
    user_id = models.CharField(max_length=8, primary_key=True)
    emp_no = models.CharField(max_length=8, unique=True)
    user_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    dept_id = models.ForeignKey(Dept, on_delete=models.DO_NOTHING)  # 부서
    position_id = models.ForeignKey(Position, on_delete=models.DO_NOTHING)  # 직급
    duty_id = models.ForeignKey(Duty, on_delete=models.DO_NOTHING)  # 직책

    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # aadminuser;nonsuper-user
    admin = models.BooleanField(default=False)  # asuperuser

    status = models.IntegerField(default=1)  # 1:재직,2:휴직,3:퇴직
    office_phone = models.CharField(max_length=255)
    mobile_phone = models.CharField(max_length=255)
