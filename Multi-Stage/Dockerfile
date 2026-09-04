################STAGE1
FROM python AS stage1
RUN apt update -y && pip install flask

###############STAGE2
FROM python:3.13-slim
WORKDIR /app
COPY app.py .
COPY --from=stage1 /usr/local /usr/local
RUN useradd -m abbas && chown -R abbas:abbas /app
USER abbas
EXPOSE 5000
CMD ["python","app.py"]
