'''This script can be used to quickly format and check for coding best practices'''
import argparse
import os
import subprocess
import sys
import constants


pip_install_cmd = [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
subprocess.run(pip_install_cmd, stdout=subprocess.PIPE)


def analyze_script(command_to_run, script_to_analyze, analyze_output_file=None, write_to_file=True, write_file_info=False):
    '''Takes in command to run, script for which we need to analyze and output file.
        Returns none and writes the analysis results to the file.
    '''
    print(f"Analyzing {script_to_analyze} using {command_to_run}")
    if write_to_file and analyze_output_file is None: raise Exception("Need output file path to write the results")
    if write_to_file and write_file_info:
        with open(analyze_output_file, "w") as wf:
            wf.write(constants.FILE_INFO)
    current_command = code_check_commands[command_to_run].copy()
    current_command.append(script_to_analyze)
    if command_to_run == f"{constants.hardcodes_cmd}{constants.cmd_suffix}":
        current_command.append("-o")
    result = subprocess.run(current_command, capture_output=True)
    current_command_output = result.stdout.splitlines()
    if command_to_run == f"{constants.black_cmd}{constants.cmd_suffix}":
        current_command_output = result.stderr.splitlines()
    if write_to_file:
        with open(analyze_output_file, "a") as wf:
            wf.write(f"\n\n{command_to_run}\n****************\n")
            for output_line in current_command_output:
                wf.write(f"{output_line}\n")
    else:
        print(current_command_output)


code_check_commands = {}
code_check_commands[f"{constants.isort_cmd}{constants.cmd_suffix}"] = [
    constants.isort_cmd
]
code_check_commands[f"{constants.black_cmd}{constants.cmd_suffix}"] = [
    constants.black_cmd
]
code_check_commands[f"{constants.flake8_cmd}{constants.cmd_suffix}"] = [
    constants.flake8_cmd
]
code_check_commands[f"{constants.interrogate_cmd}{constants.cmd_suffix}"] = [
    constants.interrogate_cmd,
    "-vv",
    "-i",
]
code_check_commands[f"{constants.whispers_cmd}{constants.cmd_suffix}"] = [
    constants.whispers_cmd
]
code_check_commands[f"{constants.hardcodes_cmd}{constants.cmd_suffix}"] = [
    sys.executable,
    constants.hardcodes_py_entry,
]
code_check_commands[f"{constants.pylint_cmd}{constants.cmd_suffix}"] = [
    constants.pylint_cmd,
    "--enable=all"
]

cmd_order = constants.COMMANDS_ORDER

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--scripts-path", type=str, default=None)
    parser.add_argument("--output-path", type=str, default=None)
    args, _ = parser.parse_known_args()

    current_directory = args.scripts_path
    analysis_output_path = args.output_path
    if current_directory is None:
        current_directory = os.getcwd()
    if analysis_output_path is None:
        analysis_output_path = os.path.join(os.getcwd(), constants.default_output_folder)

    isExist = os.path.exists(analysis_output_path)
    if not isExist:
        os.makedirs(analysis_output_path)

    scripts_to_check = [f for f in os.listdir(current_directory) if f.endswith(".py")]
    for script_name in scripts_to_check:
        write_file_info = True
        file_name = os.path.join(current_directory, script_name)
        output_file = f"{os.path.join(analysis_output_path,script_name)}{constants.output_file_extension}"
        for i, e in enumerate(cmd_order):
            analyze_script(e, file_name, output_file,write_file_info=write_file_info)
            if write_file_info: write_file_info = False
