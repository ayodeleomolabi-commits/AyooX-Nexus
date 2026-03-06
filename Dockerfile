FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install streamlit
EXPOSE 8080
CMD python3 handshake_sim.py & streamlit run dashboard.py --server.port=8080 --server.address=0.0.0.0
