# runs flask app
from flask import Flask, render_template, request

from repos.api import repos_with_most_stars
from repos.exceptions import GitHubApiException

app = Flask(__name__)
available_languages = ["Python", "JavaScript", "Ruby", "Java"]

#this is called whenever any post or get methods are called. 
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        #they request data with already present input 
        #(i.e. no languages on first load)
        selected_languages = available_languages
    elif request.method == 'POST':
        #code for post
        selected_languages = request.form.getlist("languages")

    results = repos_with_most_stars(selected_languages)
    return render_template(
        'index.html',
        selected_languages=selected_languages,
        available_languages=available_languages,
        results=results
    )
    
@app.errorhandler(GitHubApiException)
def handle_api_error(error):
    return render_template('error.html', message=error)
