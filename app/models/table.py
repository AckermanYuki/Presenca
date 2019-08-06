from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    matricula = db.Column(db.Integer, unique=True)
    password = db.Column(db.String)
    email = db.Column(db.String)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, username, matricula, password, email):
        self.username = username
        self.matricula = matricula
        self.password = password
        self.email = email

        def __repr__(self):
            return "<User %r>" % self.username

class Sprint(db.Model):
    __tablename__ = "sprints"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    relatorio = db.Column(db.String)
    objetivo = db.Column(db.String)
    data = db.Column(db.String)
    area = db.Column(db.String)
    status = db.Column(db.String)
    horario_inicio = db.Column(db.String)
    horario_termino = db.Column(db.String)

    def __init__(self, nome, relatorio, objetivo, data, area, status, horario_inicio, horario_termino):
        self.nome = nome
        self.relatorio = relatorio
        self.objetivo = objetivo
        self.data = data
        self.area = area
        self.status = status
        self.horario_inicio = horario_inicio
        self.horario_termino = horario_termino

        def __repr__(self):
            return "<Sprint %r>" % self.id

class Adm(db.Model):
    __tablename__ = "adms"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    senha = db.Column(db.String)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

        def __repr__(self):
            return "<Adm %r>" % self.id
