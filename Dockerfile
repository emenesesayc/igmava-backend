FROM wesbarnett/apache-flask:bionic-x86_64

COPY ./apache/* /etc/apache2/sites-available/
RUN a2ensite igmava igmava-ssl

# Copy application itself, changing ownership of files
COPY --chown=www-data application /var/www/igamava/application

