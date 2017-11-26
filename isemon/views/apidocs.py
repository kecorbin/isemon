from flask import render_template


def swagger_ui():
    return render_template('apidocs.html', title="API Documentation")
