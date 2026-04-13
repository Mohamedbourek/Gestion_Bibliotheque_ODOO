FROM odoo:12.0

USER root

# Copier les dépendances Python custom (si tu en as)
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt 2>/dev/null || true

# Copier ta configuration Odoo
COPY odoo.conf /etc/odoo/odoo.conf

# Copier ton module de gestion bibliothèque
COPY addons/ /mnt/extra-addons/

# Permissions correctes
RUN chown -R odoo:odoo /mnt/extra-addons

USER odoo

EXPOSE 8069

CMD ["/usr/bin/odoo", "--config=/etc/odoo/odoo.conf"]
