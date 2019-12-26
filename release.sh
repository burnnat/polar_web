# Version numbers in setup.py and __init__.py should be updated prior to running this script.
# Also, the version number changes should be committed to git and pushed (either before or after).
rm dist/*
source venv/bin/activate
python setup.py sdist bdist_wheel
twine upload dist/*