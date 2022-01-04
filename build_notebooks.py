import glob
import subprocess

subprocess.run(['which', 'python3'])
subprocess.run(['jupyter', '--version'])

notebooks = glob.glob('./**/*.ipynb', recursive=True)
notebooks = [notebook for notebook in notebooks if 'venv' not in notebook]
print('found ' + str(len(notebooks)) + ' notebooks')

for notebook in notebooks:
    out_path = notebook[1:]
    out_path = '/'.join(out_path.split('/')[0:-1])
    print('building notebook ' + notebook)
    subprocess.run(
        ['jupyter', 'nbconvert', '--execute', notebook, '--to', 'html', '--output-dir', './build' + out_path])
