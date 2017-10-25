"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)
    student_projects = hackbright.get_grades_by_github(github)


    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           student_projects=student_projects)
    return html


@app.route('/student-search')
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route('/student-add')
def student_add():
    """add a student - receiving user input"""

    return render_template('student_add.html')


@app.route('/make-student', methods=['POST'])
def make_student():
    """adding student to DB"""

    github = request.form.get('github')
    fname = request.form.get('first_name')
    lname = request.form.get('last_name')

    hackbright.make_new_student(fname, lname, github)

    return render_template('confirmation.html',
                           github=github,
                           fname=fname,
                           lname=lname)

@app.route('/project')
def display_projects():
    """display projects"""

    title, description, max_grade = hackbright.get_project_by_title(title)

    return render_template('project_info.html', title=title,
                                                description=description,
                                                max_grade=max_grade)

#need to link title argument in get_project_by_title to parameter


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
