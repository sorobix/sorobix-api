FROM python:3.11
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs >> rustup-init.sh
RUN chmod +x rustup-init.sh
RUN sh rustup-init.sh -y
RUN . "$HOME/.cargo/env"
ENV PATH="/root/.cargo/bin:$PATH"
RUN rustup target add wasm32-unknown-unknown
RUN echo $PATH
RUN curl -LJO https://github.com/stellar/soroban-tools/releases/download/v0.6.0/soroban-cli-0.6.0-x86_64-unknown-linux-gnu
RUN mv soroban-cli-0.6.0-x86_64-unknown-linux-gnu soroban
RUN chmod +x soroban
RUN mv soroban /usr/local/bin
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 3001
CMD ["python","wsgi.py"]
