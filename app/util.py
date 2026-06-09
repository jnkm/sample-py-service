import subprocess


def run_report(report_name):
    # Command injection via shell=True (UNCHANGED across commits)
    cmd = "generate_report " + report_name
    return subprocess.call(cmd, shell=True)
