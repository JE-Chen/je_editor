import subprocess


def run_on_shell(run_source, show_result_ui_function, show_result_error_function):
    try:
        exec_result = subprocess.getoutput(run_source)
        show_result_ui_function(exec_result)
    except Exception as error:
        show_result_error_function(str(error))
        raise error
