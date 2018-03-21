"""A madlib game that compliments its users."""


from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/play')
def play_game():
    """Ask user if they want to play a game."""

    player = request.args.get("person")
    play = request.args.get("play")
    return render_template("playgame.html",
                           person=player,
                           play_game=play)


@app.route('/game')
def show_madlib_form():
    """get user response"""
    play_game = request.args.get("play")
    player = request.args.get("person")
    if play_game == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html",
                               person=player)


@app.route('/madlib')
def show_madlib():
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    player = request.args.get("person")
    return render_template("madlib.html", color=color, noun=noun,
                           adjective=adjective, person=player)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
