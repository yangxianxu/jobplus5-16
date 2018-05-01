from flask import Blueprint

job = Blueprint('job', __name__, url_prefix='/job')

@job.route('/')
def index():
    page = request.args.get('page',default=1,type=int)
    pagination = Course.query.paginate(
        page=page,
        per_page=current_app.config['INDEX_PER_PAGE'],
        error_out=False
        )
    return render_template('job.html',pagination=pagination)
