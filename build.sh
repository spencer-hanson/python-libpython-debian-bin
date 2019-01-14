rm -rf build
rm -rf dist/*
python setup.py bdist_wheel -p manylinux1_x86_64
