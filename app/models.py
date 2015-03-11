# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modi
#    fy, and delete the table
# Feel free to rename the models, but don't rename db_table values or field name
#  s.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app
#   _label]'
# into your database.

from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)

    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class NflTeam(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    team_name = models.CharField(max_length=45, blank=True)
    city = models.CharField(max_length=45, blank=True)
    arena = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'nfl_team'

class Players(models.Model):
    players_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    college = models.CharField(max_length=45, blank=True)
    position = models.CharField(max_length=15, blank=True)
    fantasy_points = models.CharField(max_length=45, blank=True)
    nfl_team = models.ForeignKey(NflTeam)

    class Meta:
        managed = False
        db_table = 'players'
		
class Season(models.Model):
    season_id = models.IntegerField(primary_key=True)
    season = models.CharField(max_length=45, blank=True)
    sport = models.CharField(max_length=15, blank=True)
    superbowl = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'season'
		
class PlayerSeason(models.Model):
	players_id = models.IntegerField(primary_key=True)
	season_id = models.IntegerField(primary_key=True)
	
	class Meta:
		managed = False
		db_table = 'player_season'


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user = models.CharField(max_length=45, blank=True)
    age = models.IntegerField(blank=True, null=True)
    rank = models.CharField(max_length=45, blank=True)
    league = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserRoster(models.Model):
	user_id = models.IntegerField(primary_key=True)
	players_id = models.IntegerField(primary_key=True)
	
	class Meta:
		managed = False
		db_table = 'user_roster'

