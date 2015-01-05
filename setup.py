from setuptools import setup
setup(
    name='Showtime',
    version='0.1',
    packages=['showtime'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "Flask",
        "Flask-Admin",
        "Flask-Login",
        "Flask-Migrate",
        "Flask-OAuthlib",
        "Flask-Script",
        "Flask-SQLAlchemy",
        "pytvdbapi"
    ],
    entry_points = {
        'console_scripts': [
            "showtime_manage = showtime.tasks:manager.run"
        ]
    },
    package_data={
        'static': 'showtime/static/*',
        'templates': 'showtime/templates/*'
    }
)