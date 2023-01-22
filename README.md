# Sorobix

> Online IDE to compile, deploy, and invoke Soroban Smart Contracts on-the-fly on the Stellar network

## How it works

Sorobix provides the user an IDE on the cloud freely accessible to access and interact with the Smart Contracts on Soroban. We provide in-house support for
- Account Creation on FutureNet
- Faucet Money Deposits via FriendBot
- Compiling Rust smart contracts on the web
- Deploying these smart contracts on the Futurenet
- Invoking existing deployed smart contracts using their Contract ID

We beleive this will take the Soroban Smart Contracts to new horizons as the community can now try out Soroban on-to-go with 0 local setup! With endless possibilites of integrating this in the existing ecosystem, for example, integrating these with our official Soroban documentation, and many more, we aim to take Sorobix and Soroban hand-in-hand to newer heights!


## Tech Stack
- Python
- Shell
- ReactJS
- FastAPI
- Azure
- FutureNet
- Soroban Tools


## Local Setup

1. Clone this repo using `git clone https://github.com/ShubhamPalriwala/sorobix`
2. Make sure you have docker and rust toolchain installed
3. Run the following command to start a node connected via the chain through RPC:
    ```bash
    docker run --rm -it \
    -p 8001:8000 \
    --name stellar \
    stellar/quickstart:soroban-dev \
    --futurenet \
    --enable-soroban-rpc
    ```
4. Start the FastAPI instance:
   ```bash
    uvicorn main:app --reload
   ```
5. Start the ReactJs instance:
   ```bash
   CRA starter command here
   ```


## License

Licensed under MIT License : https://opensource.org/licenses/MIT

<p align="center">Made with ❤ by Team Gavakshi</p>