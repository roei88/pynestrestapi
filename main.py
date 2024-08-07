import uvicorn

if __name__ == '__main__':
    uvicorn.run(
        'src.app_module:http_server',
        host="0.0.0.0",
        port=443,
        reload=True,
        ssl_certfile='src/cert.pem',
        ssl_keyfile='src/key.pem'
    )
    
