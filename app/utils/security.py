import os

ALLOWED_EXTENSIONS = ['png','jpg','jpeg','PDF']


# file path check for file download request
def is_naughty(filepath, basepath, suffix):
    base_dir_abs = os.path.abspath(basepath)
    file_path_abs = os.path.abspath(filepath)
    return not (file_path_abs.startswith(base_dir_abs) and
                file_path_abs.endswith(suffix) and
                os.path.exists(file_path_abs))


# file extension check for file upload
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS