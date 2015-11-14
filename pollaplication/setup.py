from setuptools import setup

setup(name='pollaplication',
	version='0.1',
	description='Web application about polls',
	url='https://github.com/acasadoquijada/pollaplication',
	author='Alejandro Casado Quijada',
	author_email='acasadoquijada@gmail.com',
	license='GNU GPL',
	packages=['pollaplication'],
	install_requires=['django','wheel','djangorestframework'],
	zip_safe=False)
