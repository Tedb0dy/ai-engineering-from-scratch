FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# CPU-only PyTorch (fill this in: package + the CPU index URL)
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Everything else for the course + this lesson's exercises
RUN pip install numpy pandas scikit-learn matplotlib jupyter qdrant-client flask

WORKDIR /workspace
EXPOSE 8888
CMD ["python"]
