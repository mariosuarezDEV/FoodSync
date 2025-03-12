FROM python:3.12-bullseye

ENV PYTHONUNBUFFERED 1

WORKDIR /app
# [Optional] If your requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
COPY ../requirements.txt .
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp
RUN pip install --no-cache-dir -r requirements.txt
# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

COPY .. .
EXPOSE 5000
CMD ["gunicorn", "foodsync.wsgi:application", "--bind", "0.0.0.0:5000"]