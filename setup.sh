mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"gomide.gmg@gmail.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
