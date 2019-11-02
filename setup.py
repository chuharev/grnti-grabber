from setuptools import setup

setup(name='grnti-grabber',
      version='0.2',
      description='GRNTI stands for russian science classification system',
      url='https://github.com/chuharev/grnti-grabber',
      author='Alexey Chuharev',
      author_email='email@example.com',
      license='MIT',
      scripts=[
            'bin/grnti-download',
            'bin/grnti-plain2xml'
      ],
      packages=[
            'grnti-grabber'
      ],
      install_requires=[
            'bs4',
            'xmljson'
      ],
      include_package_data=True,
      zip_safe=False)
