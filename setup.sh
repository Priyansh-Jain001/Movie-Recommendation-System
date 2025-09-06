#!/bin/bash
mkdir -p ~/.streamlit/

cat <<EOT > ~/.streamlit/config.toml
[server]
headless = true
enableCORS = false
port = $PORT
EOT
