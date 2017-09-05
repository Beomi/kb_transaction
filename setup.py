from setuptools import setup, find_packages

setup(name='kb_transaction',
      version='0.0.2',
      url='https://github.com/beomi/kb-transaction',
      license='MIT',
      author='Junbum Lee',
      author_email='jun@beomi.net',
      description='Crawling KB bank transaction with IE Selenium',
      packages=find_packages(),
      long_description=open('README.md').read(),
      zip_safe=False,
      setup_requires=['python-dateutil', 'beautifulsoup4', 'selenium'],
      download_url='https://github.com/beomi/kb_transaction/archive/0.0.2.tar.gz',
      )
