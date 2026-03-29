# =============================================================
# Dockerfile
# =============================================================
# Changes from original:
#   - Added non-root user for security
#   - Created /app/instance directory for the SQLite DB file
#   - Added HEALTHCHECK so Docker knows when the app is ready
#   - Switched CMD to gunicorn (production-grade WSGI server)
#   - Added .dockerignore recommendation in comments
# =============================================================

FROM python:3.11-slim

# Create a non-root user to run the app (security best practice)
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

WORKDIR /app

# Copy requirements first so Docker can cache this layer
# (only re-runs pip install when requirements.txt changes)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Create the instance folder where SQLite will store tasks.db
# Give ownership to the non-root user
RUN mkdir -p /app/instance && chown -R appuser:appgroup /app/instance

# Switch to non-root user
USER appuser

# Tell Docker which port the app listens on (documentation only)
EXPOSE 5000

# Health check — Docker will mark container unhealthy if the app stops responding
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000')"

# Use gunicorn instead of `python app.py` for production
# 2 worker processes, binding to all interfaces on port 5000
CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:5000", "app:app"]