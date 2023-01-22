rm -rf ./sorobix_temp

cargo new --lib sorobix_temp

cd sorobix_temp

echo """
[package]
name = \"sorobix_temp\"
version = \"0.1.0\"
edition = \"2021\"

[lib]
crate-type = [\"cdylib\"]

[features]
testutils = [\"soroban-sdk/testutils\"]

[dependencies]
soroban-sdk = \"0.4.2\"

[dev_dependencies]
soroban-sdk = { version = \"0.4.2\", features = [\"testutils\"] }

[profile.release]
opt-level = \"z\"
overflow-checks = true
debug = 0
strip = \"symbols\"
debug-assertions = false
panic = \"abort\"
codegen-units = 1
lto = true

[profile.release-with-logs]
inherits = \"release\"
debug-assertions = true
""" > Cargo.toml

echo $1 > src/lib.rs

cargo build --target wasm32-unknown-unknown --release

soroban deploy \
    --wasm target/wasm32-unknown-unknown/release/sorobix_temp.wasm \
    --secret-key $2 \
    --rpc-url http://localhost:8000/soroban/rpc \
    --network-passphrase 'Test SDF Future Network ; October 2022'
