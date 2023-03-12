# Sorobix

<p align="center">
  <a href="https://github.com/ShubhamPalriwala/sorobix">
    <img src="./assets/logo.png" alt="Logo" width="380" height="190">
  </a>
</p>

> Online IDE to compile, deploy, and invoke Soroban Smart Contracts on-the-fly on the Stellar network

## Try it out:
https://sorobix.vercel.app/

## How it works

Sorobix provides the user an IDE on the cloud freely accessible to access and interact with the Smart Contracts on Soroban. We provide in-house support for
- Account Creation on FutureNet
- Faucet Money Deposits via FriendBot
- Compiling Rust smart contracts on the web
- Deploying these smart contracts on the Futurenet
- Invoking existing deployed smart contracts using their Contract ID

We beleive this will take the Soroban Smart Contracts to new horizons as the community can now try out Soroban on-to-go with 0 local setup! With endless possibilites of integrating this in the existing ecosystem, for example, integrating these with our official Soroban documentation, and many more, we aim to take Sorobix and Soroban hand-in-hand to newer heights!

![arch](assets/arch.jpeg)

## Tech Stack
- Python
- Shell
- ReactJS
- FastAPI
- FutureNet
- Soroban Tools

## Useful Links
[Sorobix-Frontend](https://github.com/RishabhKeshan/sorobix)

[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/11026000-1db07f2e-a781-4c46-8ac6-55663f9e5555?action=collection%2Ffork&collection-url=entityId%3D11026000-1db07f2e-a781-4c46-8ac6-55663f9e5555%26entityType%3Dcollection%26workspaceId%3D1e8c1d95-bc24-4d88-a958-35aaa1eee5d7)

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


## License

Licensed under MIT License : https://opensource.org/licenses/MIT

<p align="center">Made with ❤ by Team Gavakshi</p>
