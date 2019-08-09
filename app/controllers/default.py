from flask import render_template, flash, request,redirect, url_for
from flask_login import login_user, logout_user
from app import app, db, lm
from app.models.table import User,Sprint, Adm
from app.models.forms import LoginForm, LoginAdm


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first() or Adm.query.filter_by(id=id).first()

@app.route("/")
def indexlogin():
    return render_template('index_login.html')

@app.route("/index", methods=["GET","POST"])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(matricula=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for("cadastro"))
        else:
            return redirect(url_for("index", form=form))
    return render_template('index.html', form=form)

@app.route("/loginadm", methods=["GET","POST"])
def adm():
    form = LoginAdm()
    if form.validate_on_submit():
        adm = Adm.query.filter_by(email=form.email.data).first()
        if adm and adm.senha == form.senha.data:
            login_user(adm)
            return render_template('professor.html')
        else:
            return redirect(url_for("adm", form=form))
    return render_template('loginadm.html', form=form)

@app.route("/cadaluno", methods=["GET","POST"])
def aluno():
    if request.method == "POST":
        nome = request.form.get("nome")
        matricula = request.form.get("matricula")
        email = request.form.get("email")
        senha = request.form.get("senha")

        if nome and matricula and senha and email:
            alu = User(nome, matricula, senha, email)
            db.session.add(alu)
            db.session.commit()
            return render_template('professor.html')
        return redirect(url_for("aluno"))
    else:
        return render_template('cadastro_aluno.html')

@app.route("/cadastro", methods=["GET","POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome")
        relatorio = request.form.get("relatorio")
        objetivo = request.form.get("objetivo")
        data = request.form.get("data")
        area = request.form.get("area")
        status = request.form.get("status")
        horario_inicio = request.form.get("entrada")
        horario_termino = request.form.get("saida")

        if nome and relatorio and objetivo and data and area and status and horario_inicio and horario_termino:
            cad = Sprint(nome, relatorio, objetivo, data, area, status, horario_inicio, horario_termino)
            db.session.add(cad)
            db.session.commit()
        return redirect(url_for("logout"))
    else:
        return render_template('cadastro.html')


@app.route("/teste/<info>")
@app.route("/teste", defaults={"info":None})
def teste(info):
    i = Post("ana","aana","aa@aa",1)
    db.session.add(i)
    db.session.commit()
    return "ok"

@app.route("/lista", methods=["GET","POST"])
def lista():
    r = Sprint.query.all()
    return render_template('lista.html', r=r)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("indexlogin"))
