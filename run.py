from flask import Flask, Flask, render_template, flash, url_for, redirect, jsonify, request
from flask import render_template
from Newsletter_add_form import Newsletter_AddForm
from Article_add_form import ArticleForm
from werkzeug.datastructures import MultiDict
import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = "qxf2"

@app.route('/')
def index():
    return render_template('home.html')

@app.route("/add-newsletter",methods=["GET","POST"])
def Add_newsletter():
    "This page contains the form into which user enters the newsletter subject"
    form = Newsletter_AddForm()
    if form.validate_on_submit():
        subject = form.subject.data
        preview_text = form.preview_text
        flash(f'Form submitted successfully', 'success')
        return redirect(url_for("Add_articles"))
    return render_template('add_newsletter.html',form=form)

@app.route("/add-articles",methods=["GET","POST"])
def Add_articles():
    "This page contains the form where user can add articles"

    form = ArticleForm()

    if form.validate_on_submit():
        category=form.category.data
        url= form.url.data
        description=form.description.data
        reading_time=form.reading_time.data
        opener= form.opener.data

        if form.add_more.data:
            if form.category.data=="Select Category":
                flash(f'Please select category')
                return redirect(url_for("Add_articles"))
            else:
                file1 = open("replica_db.txt", "a")  # append mode
                file1.write("%s\t%s\t%s\t%s\n"%(category,url,description,reading_time))
                file1.close()
                return redirect(url_for("Add_articles"))

        if form.schedule.data:
            if opener:
                flash(f'Form submitted successfully', 'success')
                return redirect(url_for("index"))
            else:
                flash(f'Please enter the opener')
    return render_template('add_article.html',form=form)

@app.route("/url/<category>")
def url(category):
    "This page fetches url based on category selected"

    if category == "Comic":
        url = ["comic_url1","comic_url2"]
    elif category == "Articles from this week":
        url = ["thisweek_url1","thisweek_url2"]
    elif category == "Articles from past":
        url= ["past_url1", "past_url2"]
    elif category == "Automation corner":
        url=["Automation_url1", "Automation_url2"]

    return jsonify(url)

@app.route("/description/<url>")
def description(url):
    "This page fetches the article description based on url selected"

    if url=="comic_url1":
        description = "Test comic1"
    if url=="comic_url2":
        description = "Test comic 2"
    if url=="thisweek_url1":
        description = "this week article 1"
    if url=="thisweek_url2":
        description = "this week article 2"
    if url=="past_url1":
        description = "past week article 2"
    if url=="past_url2":
        description = "past week article 2"

    return jsonify(description)

@app.route("/readingtime/<url>")
def reading_time(url):
    "This article fetched reading time based on url selected"

    if url=="thisweek_url1":
        reading_time = "10 mins"
    if url=="thisweek_url2":
        reading_time = "20 mins"
    if url=="past_url1":
        reading_time = "30 mins"
    if url=="past_url2":
        reading_time = "40 mins"

    return jsonify(reading_time)


if __name__ == '__main__':
    app.run(debug=True)
