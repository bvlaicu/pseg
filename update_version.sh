git flow release start v$1
sed -i -e "s/__version__ = '.*'/__version__ = '$1'/g" pseg/__init__.py
rm -rf docs/generated
python setup.py develop
make docs
cd docs && make html && cd ..
git commit docs pseg/__init__.py -m "Update to version v$1"
git flow release finish v$1
python setup.py sdist bdist_wheel upload -r pypi
python setup.py upload_docs -r pypi
