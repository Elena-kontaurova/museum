from peewee import Model, MySQLDatabase, CharField, IntegerField, \
                   DateTimeField, AutoField, ForeignKeyField

db = MySQLDatabase("musuem", user='root', password='lenok',
                   host='localhost', port=3306)


class DataBase(Model):
    class Meta:
        database = db


class Exposition(DataBase):
    ''' экспонозиция'''
    id = AutoField()
    title = CharField()
    description = CharField()
    start_date = CharField()
    end_date = CharField()
    location = CharField()
    created_at = DateTimeField()


class Authors(DataBase):
    ''' аторы'''
    id = AutoField(primary_key=True)
    first_name = CharField()
    last_name = CharField()
    birth_date = CharField()
    death_date = CharField()
    country = CharField()
    biography = CharField()
    created_at = DateTimeField()


class Exhibit(DataBase):
    ''' экспонат'''
    id = AutoField(primary_key=True)
    title = CharField()
    description = CharField()
    creation_year = IntegerField()
    material = CharField()
    dimensions = CharField()
    value = IntegerField()
    condition = CharField()
    exposishi = CharField()
    image = CharField()
    aftor = ForeignKeyField(Authors)
    exposition = ForeignKeyField(Exposition)


class Authorization(DataBase):
    ''' авторизация'''
    id = AutoField()
    login = CharField()
    password = CharField()


class Role(DataBase):
    id = AutoField()
    id_user = ForeignKeyField(Authorization)
    role = CharField()


db.connect()
db.create_tables([Exposition, Authors, Exhibit,
                  Role, Authorization], safe=True)
db.close
