# Use Python 3.6 or later as a base image
FROM python:3.6
# Copy contents into image
COPY . .
# Install pip dependencies from requirements
RUN pip install -r requirements.txt

EXPOSE 5000
# Create an entrypoint
ENTRYPOINT ["python", "app.py"]

