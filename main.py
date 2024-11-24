from flask import Flask, redirect

app = Flask(__name__)

REDIRECTS = {
    'alliance-duel': 'https://onedrive.live.com/view.aspx?resid=E2B14D0055DFD195!928&authkey=!AGrueymaK74JlB4',
    'ad': 'https://onedrive.live.com/view.aspx?resid=E2B14D0055DFD195!928&authkey=!AGrueymaK74JlB4',
    'arms-race': 'https://www.google.com/url?q=https://1drv.ms/b/s!ApXR31UATbHihxeUBB7vjcuuPfim&sa=D&source=editors&ust=1731634807746009&usg=AOvVaw0H9N4ktDDOHPzotB8LnWIJ',
    'ar': 'https://www.google.com/url?q=https://1drv.ms/b/s!ApXR31UATbHihxeUBB7vjcuuPfim&sa=D&source=editors&ust=1731634807746009&usg=AOvVaw0H9N4ktDDOHPzotB8LnWIJ',
    'capitol-defense': 'https://docs.google.com/document/d/e/2PACX-1vSJfxEs-HG1WVgqLCGfwSjlt64wvsZUfUpvUAe1uVrH-XpkIfrLLMxTHcnCTbwOBaf6SJVsC0Rehg1m/pub',
    'cd': 'https://docs.google.com/document/d/e/2PACX-1vSJfxEs-HG1WVgqLCGfwSjlt64wvsZUfUpvUAe1uVrH-XpkIfrLLMxTHcnCTbwOBaf6SJVsC0Rehg1m/pub',
    'desert-storm': 'https://docs.google.com/document/d/e/2PACX-1vR6Bok57e8gFHiON7V8C7FcWP3wSSWuNVl8hZGKLck9Ix5lYdxHzdi5XY_Wjqzbn0WjK1-vNbdRDFad/pub',
    'ds': 'https://docs.google.com/document/d/e/2PACX-1vR6Bok57e8gFHiON7V8C7FcWP3wSSWuNVl8hZGKLck9Ix5lYdxHzdi5XY_Wjqzbn0WjK1-vNbdRDFad/pub',
    'hero-guide': 'https://docs.google.com/document/d/e/2PACX-1vTQuixEW693cEUCtyKcEi3xBVAwH1i6LeRbJe60ydvDDnme-bqTYhPn-_nJagG5luhbvztrF-ZVA6yY/pub',
    'hg': 'https://docs.google.com/document/d/e/2PACX-1vTQuixEW693cEUCtyKcEi3xBVAwH1i6LeRbJe60ydvDDnme-bqTYhPn-_nJagG5luhbvztrF-ZVA6yY/pub',
    'zombie-siege': 'https://docs.google.com/document/d/e/2PACX-1vRXSZUG4zfv5t0hfr0jbyrlUn9gVNaQZk0V7aXly61sctGtQ82fvJGrs19ROdkkEMBOPxYNLtE9GaMC/pub',
    'zs': 'https://docs.google.com/document/d/e/2PACX-1vRXSZUG4zfv5t0hfr0jbyrlUn9gVNaQZk0V7aXly61sctGtQ82fvJGrs19ROdkkEMBOPxYNLtE9GaMC/pub'
}

ROOT_PAGE = 'https://docs.google.com/document/d/e/2PACX-1vSfLOiQyTu_eodf-YmeCwSGRMTsmg6izdW_daE2ENJl2uvXF-NBjPDQigqqBytoaeatvlFUz1vd-7Aq/pub'

@app.route("/")
def root():
    return redirect(ROOT_PAGE, code=302)

@app.route("/<route>")
def redirect_endpoint(route):
    if route in REDIRECTS:
        return redirect(REDIRECTS[route], code=302)
    return redirect(ROOT_PAGE, code=302)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=False)

