from flask import Flask, render_template

app = Flask(__name__)

# Configuration provisoire pour le développement.
# Cette valeur devra être remplacée par une variable d'environnement
# avant toute mise en ligne.
app.config["SECRET_KEY"] = "A_REMPLACER_AVANT_LA_MISE_EN_LIGNE"


# ==========================================
# PAGE D'ACCUEIL
# ==========================================

@app.route("/")
def accueil():
    return render_template("accueil.html")


# ==========================================
# ESPACES DES QUATRE PROFILS
# ==========================================

@app.route("/espace/enfant")
def espace_enfant():
    return render_template(
        "profils/enfant.html",
        profil="enfant",
        titre="Espace Enfant"
    )


@app.route("/espace/adolescent")
def espace_adolescent():
    return render_template(
        "profils/adolescent.html",
        profil="adolescent",
        titre="Espace Adolescent"
    )


@app.route("/espace/adulte")
def espace_adulte():
    return render_template(
        "profils/adulte.html",
        profil="adulte",
        titre="Espace Adulte"
    )


@app.route("/espace/parent")
def espace_parent():
    return render_template(
        "profils/parent.html",
        profil="parent",
        titre="Espace Parent"
    )


# ==========================================
# PAGES DE PRESENTATION
# ==========================================

@app.route("/a-propos")
def a_propos():
    return render_template("sections/a-propos.html")


@app.route("/contact")
def contact():
    return render_template("sections/contact.html")


# ==========================================
# SECTIONS DE BLOOPS
# ==========================================

@app.route("/automatisateur")
def automatisateur():
    return render_template("sections/automatisateur.html")


@app.route("/messagerie")
def messagerie():
    return render_template("sections/messagerie.html")


@app.route("/contacts")
def contacts():
    return render_template("sections/contacts.html")


@app.route("/agenda")
def agenda():
    return render_template("sections/agenda.html")


@app.route("/taches")
def taches():
    return render_template("sections/taches.html")


@app.route("/stockage")
def stockage():
    return render_template("sections/stockage.html")


@app.route("/parametres")
def parametres():
    return render_template("sections/parametres.html")


# ==========================================
# GESTION DES ERREURS
# ==========================================

@app.errorhandler(404)
def page_introuvable(error):
    return render_template("erreurs/404.html"), 404


@app.errorhandler(500)
def erreur_serveur(error):
    return render_template("erreurs/500.html"), 500


# ==========================================
# LANCEMENT DU SERVEUR
# ==========================================

if __name__ == "__main__":
    # debug=True est réservé au développement local.
    app.run(debug=True)
