def determine_locale():
    if 'language' in session:
        return session['language']
    return request.accept_languages.best_match(['en', 'es'])


babel.init_app(app, locale_selector=determine_locale)
